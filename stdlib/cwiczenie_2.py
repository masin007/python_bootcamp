import json
from urllib.request import urlopen

lokacja = input("Gdzie chcesz sprawdzic pogode? ")

with urlopen("https://www.metaweather.com/api/location/search/?query="+lokacja) as file:
    lokacja = json.loads(file.read().decode("utf-8"))

kod_lokacji = int(lokacja[0]["woeid"])


with urlopen(f"https://www.metaweather.com/api/location/{kod_lokacji}/") as file:
    pogoda = json.loads(file.read().decode("utf-8"))

prognozy = pogoda['consolidated_weather']

for prognoza in prognozy:
    print(f"Dzień: {prognoza['applicable_date']}")
    print(f"Temperatura: {prognoza['the_temp']:.1f} C")
    print(f"Wilgotnosc: {prognoza['humidity']}%")