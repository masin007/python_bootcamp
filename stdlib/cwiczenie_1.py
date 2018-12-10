import json

# obiekt = {"imie": "Jan", "wiek": 33}
#
# print(json.dumps(obiekt))
#
# napis = '{"imie": "Jan", "wiek": 33}'
# print(type(json.loads(napis)))


try:
    with open("pracownicy.json", "r") as plik:
        pracownicy = json.load(plik)
except FileNotFoundError:
    pracownicy = []

operacja = input("Co chcesz zrobic? [d - dodaj, w - wypisz ")

if operacja == "d":
    imie = input("Imie: ")
    nazwisko = input("Nazwisko: ")
    rok_ur = int(input("Rok urodzenia: "))
    pensja = float(input("Pensja: "))
    pracownicy.append({"imie": imie,
                       "nazwisko": nazwisko,
                       "rok_urodzenia": rok_ur,
                       "pensja": pensja})
    with open("pracownicy.json", "w") as plik:
        json.dump(pracownicy, plik)

elif operacja == "w":
    for nr, p in enumerate(pracownicy, 1):
        print(f"- [{nr}] {p['imie']} {p['nazwisko']} - rok: {p['rok_urodzenia']}, pensja: {p['pensja']} PLN")
