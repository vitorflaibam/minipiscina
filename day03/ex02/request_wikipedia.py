import requests, json, dewiki, sys

# https://en.wikipedia.org/w/api.php	English Wikipedia API

query = 'chocolatine'
url = "https://en.wikipedia.org/w/api.php"
params = {
            'action':'query',
            'format':'json',
            'list':'search',
            'utf8':1,
            'srsearch':query
        }

data = requests.get(url, params=params).json()
for i in data['query']['search']:
    print(i['title'], ' - Word count: ', i['wordcount'])
