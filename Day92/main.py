#Wheather app
import requests, json
timezone = "GMT"
latitude = 51.5002
longitude = -0.1262

result = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone={timezone.upper()}")

user = result.json()
print(json.dumps(user, indent=2))

#Day92 challenge
import requests, json

def getCode(code):
  if code==0:
    return "Clear sky"
  elif code==1 or code==2 or code==3:
    return "mainly clear, partially cloudy, and overcast"
  elif code==45 or code==48:
    return "fog and depositing rime fog"
  elif code==51 or code==53 or code==55:
    return "Drizzle: Light, moderate, and dense intensity"
  elif code==56 or code==57:
    return "freezing drizzle: light and dense"
  elif code==61 or code==63 or code==65:
    return "rain: slight, moderate, and heavy intensity"
  elif code==66 or code==67:
    return "freezing rain: slight and heavy"
  elif code==71 or code==73 or code==75:
    return "snow: slight, moderate, and heavy intensity"
  elif code==76 or code==77:
    return "freezing snow: slight and heavy"
  elif code==80 or code==81:
    return "mist: light and dense"
  elif code==82 or code==83:
    return "smoke: light and dense"
  elif code==85 or code==86:
    return "haze: light and dense"
  elif code==87 or code==88:
    return "sand/ dust whirls: light and dense"
  elif code==89 or code==90:
    return "fog: light and dense"
  elif code==95 or code==96:
    return "sand/ dust whirls: medium and dense"
  elif code==99 or code==100:
    return "tornado: medium and heavy"
timezone = "GMT"
latitude = 51.5002
longitude = -0.1262

result = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone={timezone.upper()}")

user = result.json()
print(json.dumps(user, indent=2))

weatherCode = user["daily"]["weathercode"][0]
min = user["daily"]["temperature_2m_min"][0]
max = user["daily"]["temperature_2m_max"][0]

print(f"{getCode(weatherCode)} \n: {min}\t : {max}")
