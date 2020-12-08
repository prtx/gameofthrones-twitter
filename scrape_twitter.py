import tweepy
import csv
import pandas as pd

## Input your credentials here
consumer_key =  "O1dEbAJQk5BvpY0oN4pgJQ"
consumer_secret = "uNklWrtuvjfAKJLiSqwsvZccoYxW7Jb22LSswpySOc"
access_token =  "77954126-8XbvqQN3KW8oyrIhRnmDvPvMT5p5POMZAqWKgjhlm"
access_token_secret = "nwO7J7dxSZ9AVYlphTiXrsoJGyN4aAjB3DrXPM4Cgp87u"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

##  Game of thrones hastags to search
search_query = "#got OR #gameofthrones OR #got8" + " -filter:retweets"

# Open/Create a file to append data
csvFile = open('data/got_s8e2_full_7.csv', 'a')

# Use csv Writer
csvWriter = csv.writer(csvFile)
csvWriter.writerow(['created_at', 'tweet_id', 'user', 'location', 'text', 'likes', 'retweets'])


## Search query API Documentation
## https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets.html

tweet_count = 0 
for tweet in tweepy.Cursor(api.search, q = search_query, count = 100, tweet_mode='extended', lang = "en", max_id=1120097271230672897).items():
   tweet_count += 1
   if tweet_count % 1000 == 0:
      print(f'{tweet_count} tweets downloaded')
   print(tweet.created_at)
   if tweet.full_text:
      csvWriter.writerow([tweet.created_at, tweet.id, tweet.user.screen_name, 
         tweet.user.location, tweet.full_text, 
         tweet.favorite_count, tweet.retweet_count])