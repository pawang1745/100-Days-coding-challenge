import requests
import openai
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
openai.api_key = 'YOUR_OPENAI_API_KEY'
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='YOUR_SPOTIFY_CLIENT_ID', client_secret='YOUR_SPOTIFY_CLIENT_SECRET'))
news_response = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_NEWS_API_KEY')
news_stories = news_response.json()['articles'][:5]
for story in news_stories:    
    summary = openai.Completion.create(
        engine="text-davinci-003",
        prompt=story['content'],
        max_tokens=50
    )
    summary_words = summary.choices[0].text.strip().split()[:3]
search_query = ' '.join(summary_words)
song_results = sp.search(q=search_query, type='track', limit=1)
if song_results['tracks']['items']:
    track_name = song_results['tracks']['items'][0]['name']
    track_url = song_results['tracks']['items'][0]['external_urls']['spotify']
    print(f"Track: {track_name}")
    print(f"Prompt words: {search_query}")
    print(f"Sample URL: {track_url}")
    print()
