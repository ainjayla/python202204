from requests import *
from pprint import pprint

with get('https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=') as response:
    otsitav = ('<quoteText>', '</quoteText>')
    pprint(response.text[response.text.index(otsitav[0]) +
                         len(otsitav[0]):response.text.index(otsitav[1])])
