# def foo(pierwszy, *reszta):
#     print("pierwszy: ", pierwszy)
#     print("reszta", reszta)
#     if reszta:
#         return pierwszy + reszta[-1]
#     return pierwszy
#
# print(foo(1))
# print(foo(1, 2))
# print(foo(1, 2, 3, 4, 5))
#
#
#
#
# reszta = [1, 2, 5, "cos tam jeszcze"]
# print(1, 2, 5, "coś tam jeszcze")
# print(*reszta)
#
#
# def druga_funkcja(**slownik):
#     if 'd' in slownik:
#         return slownik['a'] + slownik['d']
#     if slownik:
#         return slownik['a']
#     return "Zaden warunek nie jest spelniony"
#
#
#
# print(druga_funkcja())
# print('a', druga_funkcja(a=2))
# print('a i d', druga_funkcja(a=2, b=2, c=3, d=4))
#
#
# def zamien(jakis_tekst, **co_na_co):
#     for klucz in co_na_co:
#         jakis_tekst = jakis_tekst.replace(klucz, co_na_co[klucz])
#     return jakis_tekst
#
# co_na_co = {
#     "Ala": "Kot",
#     "kota": "Alę"
# }

# print(zamien("Ala ma kota", Ala="Kot", kota="Alę"))
# print(zamien("Ala ma kota", **co_na_co))



napis = "Ten $produkt kosztuje $cena"
napis2 = "Zajecia z $przedmiot zostaly odwolane"

def formatuj(*napisy, **co_na_co):
    wynik=[]
    for napis in napisy:
        for klucz in co_na_co:
            napis = napis.replace("$"+klucz, co_na_co[klucz])
        wynik.append(napis)
    if len(wynik) ==1:
        return wynik[0]
    return wynik

print(formatuj(napis, produkt="Samochod", cena="20000"))
print(formatuj(napis2, przedmiot="Fizyki"))

assert formatuj(napis, produkt="Samochod", cena="20000") == "Ten Samochod kosztuje 20000"
assert formatuj(napis2, przedmiot="Fizyki") == "Zajecia z Fizyki zostaly odwolane"
assert formatuj(napis, napis2, produkt="Samochod", cena="20000", przedmiot="Fizyki") == ["Ten Samochod kosztuje 20000","Zajecia z Fizyki zostaly odwolane" ]
