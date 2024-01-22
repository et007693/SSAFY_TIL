import requests
import pprint

key = '1ac68e506633150d73cf431978872d3b'
lat = 37.56
lon = 126.97

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}'
data = requests.get(url).json()
# print(data)

# print(data['weather'][0]['description'])
# data['weather']

print(data.get('weather'))

