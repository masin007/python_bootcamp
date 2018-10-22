

napis = input("Podaj napis: ")

SAMOGLOSKI = "aeiouy"

licznik = 0


for litera in napis.lower():
    if litera in SAMOGLOSKI:
        licznik += 1

print(licznik)





