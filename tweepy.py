import tweepy
from textblob import TextBlob

consumer_key = '4TJHhYwJQ4HanyIz3E52C7vHj'
consumer_secret = 'SqFhYjwu20kLOS4vsFHC21Q1aqJHM5hqEY7pAZpqbzR8V41uOj'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

access_token = '760745104181125120-5LdH0QJ6gF54GQVei5YewHf3wdq5Qx8'
access_token_secret = 'r9pC8jZfsABrNYaQ6RwbU8kpLxahx5llJphal2YzlUmaf'

auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
public_tweets = api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	print("")