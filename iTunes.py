import json 
import requests
import sys 

def responce():
    if le(sys.argv) != 2:
        sys.exit()
        
responce = requests.get("https://itunes.apple.com/search?entity=song&limit=100&term="+sys.argv[1])
print(json.dumps(responce.json(), indent=4))