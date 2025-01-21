#in console write:
# pip install requests
# python3 iTunes_songlist.py weezer(or different other songs)


import json
import requests
import sys

from iTunes import responce

if len(sys.argv) != 2:
    sys.exit()

responce = requests.get("https://itunes.apple.com/search?entity=song&limit=100&term="+sys.argv[1])

o = responce.json()
for result in o['results']:
    print(result['trackName'])

