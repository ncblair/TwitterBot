from datetime import datetime
from threading import Timer
import tweepy
import getQuote

consumer_key = "PUT KEY HERE"
consumer_secret = "PUT KEY HERE"

access_token = "PUT KEY HERE"
access_token_secret = "PUT KEY HERE"

x = datetime.today()

y = x.replace(day=x.day+1, hour=12, minute=30, second=0, microsecond=0)
delta_t = y - x

secs = delta_t.seconds + 1

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def quote_of_the_day():
    api.update_status(status = getQuote.get_quote())

t = Timer(secs, quote_of_the_day)
t.start()

