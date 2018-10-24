

slownik = {}

napis = input("Podaj napis: ").lower()

for litera in napis:
    if litera in slownik:
        slownik[litera] = slownik[litera] + 1
    else:
        slownik[litera] = 1

print(slownik)