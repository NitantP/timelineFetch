import configparser
import tkinter as tk
import tweepy
from tweepy import OAuthHandler


master = tk.Tk()

def fetchtimeline(event=None):
	config = configparser.ConfigParser()

	config.read('../config.ini')

	if 'api.twitter.com' in config:
		consumer_key = config['api.twitter.com']['consumer_key']
		consumer_secret = config['api.twitter.com']['consumer_secret']
		access_token = config['api.twitter.com']['access_token']
		access_secret = config['api.twitter.com']['access_secret']

	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)

	api = tweepy.API(auth)

	twitterid = inputid.get()

	for status in tweepy.Cursor(api.user_timeline, id=twitterid).items(10):
		print(status.text)
		print('------------------------------')

tk.Label(master, text='TwitterID').grid(row=0)

inputid = tk.StringVar()
e1 = tk.Entry(master, textvariable=inputid)
e1.grid(row=0, column=1)
e1.bind('<Return>', fetchtimeline)
e1.focus_set()

tk.Button(master, text='Fetch', command=fetchtimeline).grid(row=0, column=2)

master.mainloop()