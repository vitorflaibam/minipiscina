import requests, json, dewiki, sys

# https://en.wikipedia.org/w/api.php	English Wikipedia API

name = "chocolatine"
r = requests.get("https://en.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&titles=chocolatine&formatversion=2&rvprop=content&rvslots=*")

data = r.json()

print(data['parse']['text'])