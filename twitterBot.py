from datetime import datetime
from threading import Timer
import tweepy
import getQuote
import keys


x = datetime.today()

y = x.replace(day=x.day+1, hour=12, minute=30, second=0, microsecond=0)
delta_t = y - x

secs = delta_t.seconds + 1

auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy.API(auth)

def quote_of_the_day():
    quote = getQuote.get_quote()
    while len(quote) > 140:
        quote = getQuote.get_quote()
    print(quote)
    api.update_status(status = quote)
quote_of_the_day()
t = Timer(secs, quote_of_the_day)
t.start()

