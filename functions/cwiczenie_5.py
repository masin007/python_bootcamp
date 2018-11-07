lista = [10, 20, 30, 40, 50]
lista2 = [x for x in range(2000)]

def silnia(liczba):

    if liczba == 0:
        return 1
    else:
        return liczba * silnia(liczba - 1)



silnia(3)

print(silnia(3))