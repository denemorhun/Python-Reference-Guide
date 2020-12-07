import requests
# import urllib.request 
import json

urlData = 'https://earthquake.usgs.gov/fdsnws/event/1/application.json'

parameters = {'magnitudetypes' : '2'}

response = requests.get(urlData, params=parameters)

print(response.url)
print(response.content)

content = response.content

quake_info = json.loads(content)

if "title" in quake_info["metadata"]:
        print(quake_json["metadata"]["title"])