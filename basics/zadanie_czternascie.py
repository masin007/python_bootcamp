max_liczba = None
min_liczba = None

while True:

    dane = input("Podaj liczbe, jeżeli chcesz zakonczyc wcisnij k: ")
    if dane == "k":
        break

    x = int(dane)
    if max_liczba is None or x > max_liczba:
        max_liczba = x
    if min_liczba is None or x < min_liczba:
        min_liczba = x

if max_liczba is None:
    print("Nie wprowadzono danych")
else:
    print(f"Najwieksza liczba wynosi: {max_liczba}, najmniejsza liczba wynosi {min_liczba}")
