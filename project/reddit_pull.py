from IPython import get_ipython

# There are many different tools and kits used in this exploratory notebook. 
# Praw is a reddit API wrapper which is used to scrape subreddit posts and create dataframes from those posts.
# Praw

# this code cell has imports.
# praw is the reddit scraper
# pandas is pandas
import praw
import pandas as pd
from dotenv import load_dotenv
import os

#load environment variables
load_dotenv()

PRAW_CLIENT_ID = os.getenv('PRAW_CLIENT_ID')
PRAW_CLIENT_SECRET = os.getenv('PRAW_CLIENT_SECRET')
PRAW_USER_AGENT = os.getenv('PRAW_USER_AGENT')

# here is a read only reddit scraper object. This can be used to scan and scrape stories.
# the parameters below must be provided for the scraper to work.
# This is what will be used to pull stories from the reddit's online forum.
# to get credentials , do the following
# sign up for a reddit account
# go to your "prefs" 
# click on the "apps" tab
# create an app, and you'll see your client details there
# just create a .envh to hold them and you're good to go!

reddit = praw.Reddit(client_id=PRAW_CLIENT_ID,
                     client_secret=PRAW_CLIENT_SECRET,
                     user_agent=PRAW_USER_AGENT)

# The reddit API doesn't require password credentials for a read only API
# which is what we're doing. So there are no passwords being held.


# Create a blank data list
data_raw = []
# obtain 100 submissions from the policebrutality channel
for submission in reddit.subreddit("policebrutality").new(limit=100):
  print(submission.title)
  # appending the id, title, text, and url to the raw list
  data_raw.append([submission.id, submission.title, submission.selftext, submission.url])

# rename the columns to recognizable titles
col_names = ['id', 'title', 'text', 'news_url']

# This data frame holds stories from the police brutality subreddit.
# It can be created with many more stories, and can be filtered by newest posts
# or by the hottest posts.
# I recommend newest posts, because the hottest posts doesn't update as frequent
df = pd.DataFrame(data_raw, columns=col_names)

# if you want the raw data, comment this out and change the next command
output = df[['title', 'news_url']]

# If you want the raw data, just pass df instead of output 
output.to_csv('redditbrutality_posts.csv')

# I recommend investigating some other features available for pulling
# from the PRAW api. It could be helpful.

# This file should do a pull from the reddit api, and download the 
# scraped stories as a .csv in this folder. Pass this CSV through
# your classification model and then use the results to populate the
# map with news stories that are classified as police brutality.