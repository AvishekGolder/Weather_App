import requests

from pprint import pprint

API_Key = '5ec8e07d6d10fff1e83424a2a547d4b5'

city = input("Enter you city : ")

url = "https://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather = requests.get(url).json()

pprint(weather)

