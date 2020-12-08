import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key= 'zglsm0NIl0KlJh0yaB0KxcCTp'
consumer_secret = 'Cfjj95GImRLd0Wr4gChooewOLDDJ2vIxM8dSWoRHxE0z9TfOv8'
access_token = '3180412436-CcPVHqyVLJwbOI1hLLIGaTUVn9N4M9P3VqY3WkT'
access_token_secret = 'MPTwcYRpGGxZwiMW6kETICGbnL6edeENZccNYZRhOzzjO'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('got.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q=["#gameofthrones"],count=100,lang="en").items():
    print(tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
