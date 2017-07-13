import tweepy
from tweepy import OAuthHandler

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

twitterid = input('ID of timeline you want to retrieve: ')
print('------------------------------')

for status in tweepy.Cursor(api.user_timeline, id=twitterid).items(10):
	print(status.text)
	print('------------------------------')
