from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi_utils.tasks import repeat_every

from app.api import predict, viz, getdata, update, healthCheck

from pydantic import BaseModel, Field, validator
import pandas as pd
import praw
import os
import requests
from bs4 import BeautifulSoup
import re
import pickle
from newspaper import Article
import spacy
from collections import Counter
from datetime import datetime
from dotenv import load_dotenv


# set up various things to be loaded outside of the function
# geolocation data
locs_path = os.path.join(os.path.dirname(
    __file__), '..', 'cities_states.csv')
locs_df = pd.read_csv(locs_path)


def lowerify(text):
    # fix up geolocation dataframe a little
    return text.lower()


locs_df = locs_df.drop(columns=['Unnamed: 0', 'country'])
locs_df['city_ascii'] = locs_df['city_ascii'].apply(lowerify)
locs_df['admin_name'] = locs_df['admin_name'].apply(lowerify)

states_map = {}
# for each state, map their respective cities
for state in list(locs_df.admin_name.unique()):
    states_map[state] = locs_df[locs_df['admin_name']
                                == state]['city_ascii'].to_list()

# police brutality indentifying nlp
model_path = os.path.join(os.path.dirname(
    __file__), '..', 'model.pkl')
model_file = open(model_path, 'rb')
pipeline = pickle.load(model_file)
model_file.close()

# local csv backlog path
backlog_path = os.path.join(os.path.dirname(
    __file__), '..', 'backlog.csv'
)

# spacy nlp model
nlp = spacy.load('en_core_web_sm')

load_dotenv()

# globalize these variables because I need to

PRAW_CLIENT_ID = os.getenv('PRAW_CLIENT_ID')
PRAW_CLIENT_SECRET = os.getenv('PRAW_CLIENT_SECRET')
PRAW_USER_AGENT = os.getenv('PRAW_USER_AGENT')


app = FastAPI(
    title='HRF DS API Labs 27',
    description='Returns posts from different sources on police brutality',
    version='0.69',
    docs_url='/',
)

app.include_router(predict.router)
app.include_router(viz.router)
app.include_router(getdata.router)
app.include_router(update.router)
app.include_router(healthCheck.router)

@app.on_event('startup')
@repeat_every(seconds=60*60*24)  # 24 hours
def run_update() -> None:
    '''
    Update backlog database with data from reddit.
    '''
    print('Updating backlog at %s' % datetime.now())

    reddit = praw.Reddit(
        client_id= PRAW_CLIENT_ID,
        client_secret= PRAW_CLIENT_SECRET,
        user_agent= PRAW_USER_AGENT
    )
    # Grab data from reddit
    data = []
    for submission in reddit.subreddit("news").top('week', limit=500):
        data.append([
            submission.id, submission.title, submission.url
        ])
    # construct a dataframe with the data
    col_names = ['id', 'title', 'url']
    df = pd.DataFrame(data, columns=col_names)

    # pull the text from each article itself using newspaper3k
    content_list = []
    date_list = []
    # go through each URL and use newspaper3k to extract data
    for id_url in df['url']:
        # use newspaper3k to extract text
        article = Article(id_url)
        article.download()
        # if the article doesn't download, the error is thrown in parse()
        try:
            article.parse()
        except:
            # add null values to show no connection
            content_list.append(None)
            date_list.append(None)
            continue
        content_list.append(article.text)
        # this will be null if newspaper3k can't find it
        date_list.append(article.publish_date)
    df['text'] = content_list
    df['date'] = date_list

    # drop any articles with missing data columns
    df = df.dropna()
    df = df.reset_index()
    df = df.drop(columns='index')

    # convert date column to pandas Timestamps
    def timestampify(date):
        return pd.Timestamp(date, unit='s').isoformat()
    df['date'] = df['date'].apply(timestampify)

    # use NLP model to filter posts
    df['is_police_brutality'] = pipeline.predict(df['title'])
    df = df[df['is_police_brutality'] == 1]
    df = df.drop(columns='is_police_brutality')

    # use spaCy to extract location tokens
    tokens_list = []
    for text in df['text']:
        doc = nlp(text.lower())
        ents = [e.text for e in doc.ents if e.label_ == 'GPE']
        tokens_list.append(ents)
    df['tokens'] = tokens_list

    # figure out which city and state the article takes place in
    city_list = []
    state_list = []
    geo_list = []
    for tokens in df['tokens']:
        # set up Counter
        c = Counter(tokens)

        # set up geolocation dict for geo list
        geo_entry = {'lat': None, 'long': None}

        # count which states come back the most, if any
        state_counts = {}
        for state in states_map:
            if c[state] > 0:
                state_counts[state] = c[state]

        # get state(s) that came back the most as dict with lists
        max_count = 0
        max_state = None

        for state in state_counts:
            if state_counts[state] > max_count:
                max_count = state_counts[state]
                max_state = {state: {}}
            elif state_counts[state] == max_count:
                max_state[state] = {}

        # if no state is found
        if max_state is None:
            city_list.append(None)
            state_list.append(None)
            geo_list.append(geo_entry)
            continue

        max_city = None
        # get any cities in tokens based on states
        for state in max_state:  # ideally this should only run once
            city_counts = {}
            for city in states_map[state]:
                if c[city] > 0:
                    city_counts[city] = c[city]
            max_state[state] = city_counts

            # get the city/state combo that came back the most
            max_count = 0
            for city in city_counts:
                if city_counts[city] > max_count:
                    max_count = city_counts[city]
                    max_city = (city, state)

        # if no city is found
        if max_city is None:
            city_list.append(None)
            state_list.append(None)
            geo_list.append(geo_entry)
            continue

        # the city and state should be known now

        city_list.append(max_city[0].title())
        state_list.append(max_city[1].title())
        # now get the geolocation data
        row = locs_df[(
            (locs_df['city_ascii'] == max_city[0]) &
            (locs_df['admin_name'] == max_city[1])
        )]
        row = row.reset_index()
        if row.empty:
            pass
        else:
            geo_entry['lat'] = row['lat'][0]
            geo_entry['long'] = row['lng'][0]
        geo_list.append(geo_entry)

    # loop ends, add cities and states onto dataframe
    df['city'] = city_list
    df['state'] = state_list
    df['geocoding'] = geo_list

    # drop any columns with null entries for location
    df = df.dropna()
    df = df.reset_index()
    df = df.drop(columns='index')

    # cleanup to match 846 api
    def listify(text):
        return [text]
    df['links'] = df['url'].apply(listify)
    df['description'] = df['text']
    df = df.drop(columns=['tokens', 'text'])
    df = df[[
        'id', 'state', 'city',
        'date', 'title', 'description',
        'links', 'geocoding'
    ]]

    # save the file to a local csv
    df.to_csv(backlog_path, index=False)
    print("Backlog updated at %s" % datetime.now())


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    uvicorn.run(app)
