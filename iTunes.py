#in console write: 
# pip install requests
# python3 iTunes.py weezer(or different other songs)

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

responce = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term="+sys.argv[1])
print(json.dumps(responce.json()))
