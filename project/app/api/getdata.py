from fastapi import APIRouter, HTTPException
import pandas as pd
import praw
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
import re
import pickle

router = APIRouter()
load_dotenv()


@router.get('/testpath')
async def testpath():
    return {'return_code': '200'}


@router.get('/getdata')
async def getdata(pullnum: int):
    '''
    Get data from Reddit on police brutality; returns only stories
    from r/news about police brutality in JSON format.
    '''

    # start by connecting to PRAW
    PRAW_CLIENT_ID = os.getenv('PRAW_CLIENT_ID')
    PRAW_CLIENT_SECRET = os.getenv('PRAW_CLIENT_SECRET')
    PRAW_USER_AGENT = os.getenv('PRAW_USER_AGENT')
    print('.env loaded with key values of:')
    print('PRAW_CLIENT_ID:', PRAW_CLIENT_ID)
    print('PRAW_CLIENT_SECRET:', PRAW_CLIENT_SECRET)
    print('PRAW_USER_AGENT:', PRAW_USER_AGENT)
    # initialize PRAW via reddit api keys
    reddit = praw.Reddit(client_id=PRAW_CLIENT_ID,
                         client_secret=PRAW_CLIENT_SECRET,
                         user_agent=PRAW_USER_AGENT)

    # Grab data from reddit
    data = []
    for submission in reddit.subreddit("news").hot(limit=pullnum):
        data.append([submission.id, submission.title,
                     submission.url, submission.created])
    # construct a dataframe with the data
    col_names = ['id', 'title', 'url', 'created']
    df = pd.DataFrame(data, columns=col_names)
    # pull the text from each article itself
    content_list = []
    # use zip to iterate through tuples; faster than iterrows
    df_snip = df['url']
    for url in df_snip:
        # get the whole website in HTML form
        try:
            r = requests.get(url, timeout=10)
        except:
            print("ERROR: Requests had bad connection or timed out.")
            # append empty text if website can't be reached
            content_list.append('')
            continue
        # use BS4 to grab <p> tags
        soup = BeautifulSoup(r.text)
        output_text = " ".join([x.text for x in soup.find_all('p')])
        # use regex to clean up anything that isn't standard punctuation
        output_text = re.sub('[^a-zA-Z0-9.,\']+', ' ', output_text).strip()
        content_list.append(output_text)
    # create new column with text data
    df['text'] = content_list
    df = df[df['text'] != '']

    # Load an NLP model and use it to filter reddit data
    model_path = os.path.join(os.path.dirname(
        __file__), '..', '..', 'model.pkl')
    model_file = open(model_path, 'rb')
    pipeline = pickle.load(model_file)
    model_file.close()

    # use NLP model to make predictions for the posts from PRAW
    df['is_police_brutality'] = pipeline.predict(df['title'])
    df_pb = df[df['is_police_brutality'] == 1]
    df_pb = df_pb[['id', 'title', 'text', 'created']]
    return df_pb.to_json(orient='records')
