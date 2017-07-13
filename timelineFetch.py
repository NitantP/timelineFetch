import configparser
import tweepy
from tweepy import OAuthHandler

config = configparser.ConfigParser()

config.read('./../config.ini')

if 'api.twitter.com' in config:
	consumer_key = config['api.twitter.com']['consumer_key']
	consumer_secret = config['api.twitter.com']['consumer_secret']
	access_token = config['api.twitter.com']['access_token']
	access_secret = config['api.twitter.com']['access_secret']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

twitterid = input('ID of timeline you want to retrieve: ')
print('------------------------------')

for status in tweepy.Cursor(api.user_timeline, id=twitterid).items(10):
	print(status.text)
	print('------------------------------')
