
liczby = set()
while True:
    komenda = (input("Podaj liczbe, jezeli chcesz przerwac wcisnij k "))
    if komenda.lower() == "k":
            break
    else:
        liczba = int(komenda)
        liczby.add(liczba)
print(f"Unikalnych liczb jest {len(liczby)}")
liczby_parzyste = set(range(0,101,2))

print(f"W tym liczb parzystych od 0 do 100 {len(liczby & liczby_parzyste)}")


