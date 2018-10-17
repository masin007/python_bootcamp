suma = []
i = 0
while len(suma)<10:

    liczba = input("Podaj maksymalnie dziesiec liczb do obliczenia sredniej, jezeli chcesz skonczyc wcisnij k: ")
    if liczba == "k":
        break
    liczba = int(liczba)
    suma.append(liczba)


if len(suma) == 0:
    print("Nie podano zadnej liczby")
else:
    srednia = sum(suma) / len(suma)
    print(f"Srednia to {srednia}")