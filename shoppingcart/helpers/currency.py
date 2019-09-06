import typing
import httplib2
import json

def getCurr(curr):
    # USD,GBP,CAD,AUD,INR,PLN
    # Client key currently hardcoded for this example
    url = 'http://data.fixer.io/api/latest?access_key=db54d326c3f8257b1dfb211eadf1fdf5&symbols=%s' % curr
    h = httplib2.Http()
    result = json.loads(h.request(url,'GET'))[1]
    return result
