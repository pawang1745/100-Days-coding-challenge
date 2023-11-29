import requests, json 

result = requests.get("https://randomuser.me/api/")
user = result.json() 
name = f"""{user["results"][0]["name"]["first"]} {user["results"][0]["name"]["last"]}""" 
image = f"""{user["results"][0]["picture"]["medium"]}""" 
picture = requests.get(image) 
f = open("image.jpg", "wb")
f.write(picture.content) 
print(image) 

print("===============================")

result = requests.get("https://randomuser.me/api/")
user = result.json()
for person in user['results']: 
  name = f"""{person["name"]["first"]} {person["name"]["last"]}""" 
  print(name)
