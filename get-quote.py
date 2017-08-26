import json
from urllib.request import urlopen

# Get JSONified quote
result = json.load(urlopen("http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1"))

# Get only the quote
quote = result[0]['content']

# Strip off HTML tags
quote = quote.replace('<p>', '').replace('</p>', '').replace('\n', '')

print(quote)
