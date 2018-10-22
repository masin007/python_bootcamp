napis = input("Podaj napis: ")

licznik = 0
czy_zliczac = False


# for litera in napis:
#     if (napis.index(litera) > napis.index("<")) and (napis.index(litera) < napis.index(">")):
#         licznik = licznik + 1
#
# print(licznik)



for litera in napis:
    if litera == "<":
       czy_zliczac = True
    elif litera == ">":
        czy_zliczac = False
    elif czy_zliczac:
        licznik += 1

print(licznik)