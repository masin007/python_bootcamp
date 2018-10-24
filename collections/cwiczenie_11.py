
zbior = set()
while  True:
    liczba = (input("Podaj liczbe, jezeli chcesz przerwac wcisnij k "))
    if liczba == "k":
            break
    else:
        zbior.add(liczba)
print(zbior)


y = set(range(0,100, 2))