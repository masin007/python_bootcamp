
def wypisz_samogloski(napis):
    for litera in napis:
        if litera in "aeioy":
            yield litera




for x in wypisz_samogloski("ala ma kota"):
    print(x)