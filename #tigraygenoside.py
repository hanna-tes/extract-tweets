import tweepy
from tweepy import OAuthHandler
import pandas as pd
access_token = 'xxx'
access_token_secret = 'xxx'
consumer_key = 'xxx'
consumer_secret = 'xxx'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
# Define the search term variables
def scraptweets(search_words, date_since, until_date, numtweets):
    df_tweets = pd.DataFrame(columns = ['username', 'accdescri', 'location', 'following',
                                        'followers', 'totaltweets', 'usercreateti', 'tweetcreateti',
                                        'retweetcount', 'text']
                                )  
    tweets = tweepy.Cursor(api.search, q=search_words, lang="en", since=date_since, until=until_date, 
      	tweet_mode='extended').items(numtweets)

# Store these tweets into a python list
    tweet_list = [tweet for tweet in tweets]
    numtweets = 0
    for tweet in tweet_list:
# call the values
            username = tweet.user.screen_name
            accdescri = tweet.user.description
            location = tweet.user.location
            following = tweet.user.friends_count
            followers = tweet.user.followers_count
            totaltweets = tweet.user.statuses_count
            usercreateti = tweet.user.created_at
            tweetcreateti = tweet.created_at
            retweetcount = tweet.retweet_count
            try:
                text = tweet.retweeted_status.full_text
            except AttributeError:  
                text = tweet.full_text
                ith_tweet = [username, accdescri, location, following, followers, totaltweets,
                         usercreateti, tweetcreateti, retweetcount, text]
                # Append to dataframe - df_tweets
                df_tweets.loc[len(df_tweets)] = ith_tweet
                # increase counts
                numtweets += 1
    filename = 'scraped_tweets.csv'
      
           # save our data as a CSV file.
    df_tweets.to_csv(filename)
        
# Initialise the spcefic variables:
search_words = '#TigrayGenocide'
date_since = '2021-04-13'
until_date = '2021-04-15'
numtweets = 100
# Call function scraptweets
scraptweets(search_words, date_since, until_date, numtweets)





