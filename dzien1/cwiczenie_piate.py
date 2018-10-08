
miastoA = str(input("Miasto A: "))
miastoB = str(input("Miasto B: "))
dystans_AB = float(input(f"Dystans {miastoA}-{miastoB}: "))
cena_paliwa = float(input("Cena paliwa: "))
spalanie = float(input("Spalanie na 100 km: "))
koszt = int(dystans_AB * spalanie * cena_paliwa / 100)
print()
print(f"Koszt przejazdu {miastoA}-{miastoB} to {koszt} PLN")
