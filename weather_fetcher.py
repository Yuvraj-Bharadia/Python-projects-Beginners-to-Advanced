import requests

API_KEY = "0e253d2f773189e45cf5cccfdf55c71b"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ").lower()
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    print(data)
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)
    print("Weather:", weather)
    print("Temperature:", temperature)
else:
    print("an Error ocurred")