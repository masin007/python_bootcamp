
x = 0
podzielne5 = 0
podzielne3 = 0
podzielne = 0
lista1 = []
lista2 = []
lista3 = []

for x in range(101):
    if x %3 == 0:
        podzielne3 = 1 + podzielne3
        lista1.append(x)
    if x %5 == 0:
        podzielne5 = 1 + podzielne5
        lista2.append(x)
    if x %3 == 0 or x %5 == 0:
        podzielne = 1 + podzielne
        lista3.append(x)

print(f"Liczb podzielnych przez 3 jest: {podzielne3}, liczb podzielnych przez 5 jest: {podzielne5}.")
print(f"Liczb podzielnych przez 3 i przez 5 jest: {podzielne}")
print(lista1)
print(lista2)
print(lista3)