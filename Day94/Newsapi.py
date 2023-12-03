import requests, json, os
import openai

openai.organization = os.environ['organizationID']
openai.api_key = os.environ['openai']
openai.Model.list()

prompt = "Who is the most handsome bald man?"

response = openai.Completion.create(model="text-davinci-002", prompt=prompt, temperature=0, max_tokens=6)

print(response["choices"][0]["text"].strip())



newsKey = os.environ['newsapi']
country = "us"

url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={newsKey}"

result = requests.get(url)
data = result.json()
for article in data['articles']:
  print(article['title'])
  print(article['url'])
  print(article['content'])
