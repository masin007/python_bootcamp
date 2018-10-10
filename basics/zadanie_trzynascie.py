

i = 0
suma = 0

while True:

    dane = input("Podaj temperature lub k by zakonczyc: ")
    if dane == "k":
        break
    dane = float(dane)
    suma = suma + dane
    i = i + 1

srednia = suma/i
print(f"Srednia  temperatura wynosi: {srednia}")
