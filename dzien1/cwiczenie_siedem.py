liczba = int(input("Podaj liczbe: "))

print(f"Podzielna przez 2, podzielna przez 3 i wieksza od 10 lub jest to liczba 7: {liczba ==7 or (liczba%2 == 0 and liczba%3 == 0 and liczba>10)}")