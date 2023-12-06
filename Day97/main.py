import requests, os, openai
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')  # Create a BeautifulSoup object

article = soup.find_all("div", {"class":"mw-parser-output"})[1]
for section in article:
  content = section.find_all("p")

text=""
for p in content:
  text += p.text
print(text)

openai.organisation = os.environ['organisationID']
openai.api_key = os.environ['openai']
openai.Model.list()
prompt = f"Summarize the following text in no more than 3 paragraphs: {text}"
openai.completion.create(model="text-davinci-002", prompt=text, temperature=0, max_tokens=150)

refs = soup.find_all("ol", {"class":"references"})
for ref in refs:
  print(ref.text.replace("^ ", ""))

print(response["choises"][0]["text"].strip())
