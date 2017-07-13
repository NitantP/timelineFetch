import tweepy
from tweepy import OAuthHandler

consumer_key = 'JjvyKzr2I8LKC0fVzNyby2zkn'
consumer_secret = 'U8Unuae2XEp434wO2HhwyhZFi6w7XwRtK1RTPatHs5v4dulmtQ'
access_token = '465212227-tN1DXqn5lTEUHpqJ8mD6PteiuUi9FNx2I7x4pNoO'
access_secret = 'lwEdULHSqgUc6u2jUBm6VLuJdzKn5S57zfKfi4KJlh5mz'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

twitterid = input('ID of timeline you want to retrieve: ')
print('------------------------------')

for status in tweepy.Cursor(api.user_timeline, id=twitterid).items(10):
	print(status.text)
	print('------------------------------')
