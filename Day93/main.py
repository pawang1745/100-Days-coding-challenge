import requests, json, os
from requests.auth import HTTPBasicAuth

clientID = os.environ['CLIENT_ID']
clientSecret = os.environ['CLIENT_SECRET']

url = "https://accounts.spotify.com/api/token"
data = {"grant_type":"client_credentials"}
auth = HTTPBasicAuth(clientID, clientSecret)

response = requests.post(url, data=data, auth=auth)
print(response.json())

accessToken = response.json()["access_token"]

url = "https://api.spotify.com/v1/search"
headers = {'Authorization': f'Bearer {accessToken}'}

from flask import Flask
from requests.auth import HTTPBasicAuth
import requests

import os

clientID = os.environ['CLIENT_ID']
clientSecret = os.environ['CLIENT_SECRET']

url = 'https:accounts.spotify.com/api/token'
data = {"grant_type":"client_credentials"}
auth = HTTPBasicAuth(clientID, clientSecret)
response = requests.post(url, data=data, auth=auth)
accessToken = response.json()['access_token']
year = 1990
offset = 0

headers = {"Authorization": f"Bearer ' + {accessToken}"}
url = "https://api.spotify.com/v1/search?q=year:{year}&type=track&offset={offset}"
response = requests.get(url, headers=headers)
tracks = response.json()['tracks']
while tracks['next']:
    offset += 20
    url = "https://api.spotify.com/v1/search?q=year:{year}&type=track&offset={offset}"
    response = requests.get(url, headers=headers)
    tracks = response.json()['tracks']
for track in tracks['items']:
        print(track['name'])
  app = Flask(__name__)
  
  @app.route('/')
  def hello_world():
    return 'Hello, World!'
  
  if __name__ == '__main__':
    app.run()
    
