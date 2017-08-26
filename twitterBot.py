from datetime import datetime
from threading import Timer
import tweepy
import getquote

 x = datetime.today()

 y = x.replace(day=x.day+1, hour=12, minute=30, second=0, microsecond=0)
 delta_t = y - x

secs = delta_t.seconds + 1

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def quote_of_the_day():
    api.update_status(status = get-quote.get_quote())

t = Timer(secs, quote_of_the_day)
t.start()
