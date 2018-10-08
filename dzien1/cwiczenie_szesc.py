liczba = int(input("Podaj liczbe: "))


print(f"Większa od 10: {liczba > 10}")
print(f"Mniejsza rowna 15: {liczba <= 15}")
print(f"Podzielna przez 2: {liczba%2 == 0}")

print(f"Podzielna przez 3 i wieksza od 10: {liczba%3 == 0 and liczba>10}")
print(f"Wieksza od 10 lub podzielna przez 5: {liczba>10 or liczba%5 == 0}")