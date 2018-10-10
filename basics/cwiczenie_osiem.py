dlugosc = int(input("Podaj dlugosc: "))
szerokosc = int(input("Podaj szerokosc: "))
wysokosc = int(input("Podaj wysokosc: "))

objetosc = dlugosc * szerokosc * wysokosc
litr = 1000

if (objetosc > 2 * litr):
    print(f"Objetosc opakowania wynosi {objetosc} i jest wieksza niz dwa litry (2000)")
elif objetosc > litr
    print(f"Objetosc opakowania wynosi {objetosc} i jest wieksza niz litr (1000)")
else:
    print(f"Objetosc opakowania wynosi {objetosc} i jest mniejsza lub rowna litrowi (1000)")

