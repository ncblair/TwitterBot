import json
import codecs
from urllib.request import urlopen


def get_quote():

    reader = codecs.getreader("utf-8");
    # Get JSONified quote
    result = json.load(reader(urlopen("http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1")))

    # Get only the quote
    quote = result[0]['content']

    # Strip off HTML tags
    quote = quote.replace('<p>', '').replace('</p>', '').replace('\n', '')
    return quote
