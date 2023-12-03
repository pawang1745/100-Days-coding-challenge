import requests, json, os
import openai

openai.organization = os.environ['organizationID']
openai.api_key = os.environ['openai']

newsKey = os.environ['newsapi']
country = "us"

# Get all the news stories for the day from NewsAPI
url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={newsKey}"
result = requests.get(url)
data = result.json()

# Send off a request to openai to summarize the stories
prompt = "Summarize the top news stories for the day:\n"
for article in data['articles']:
    prompt += f"- {article['title']}\n{article['content']}\n\n"

response = openai.Completion.create(model="text-davinci-002", prompt=prompt, temperature=0, max_tokens=150)

# Display the top 5 news stories for the day along with a summary of each story
for i, article in enumerate(data['articles'][:5]):
    print(f"Story {i+1}: {article['title']}")
    print(f"Summary: {response['choices'][0]['text'].split('Story')[i+1].strip()}\n")
