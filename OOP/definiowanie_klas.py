

class Animal:
    krolestwo = "Fauna" #atrybut klasowy

    def _init_(self, nazwa):
        self.nazwa = nazwa

a1 = Animal("Zyrafa")   #instancja klasy
a2 = Animal("Mysz")     #instancja klasy

print(a1.krolestwo)
print(a2.krolestwo)

print(a1.nazwa)
print(a2.nazwa)


# zyrafa = Animal()   #instancja klasy
# mysz = Animal()     #instancja klasy
# print(type(mysz))
# print(zyrafa.krolestwo)
# print(mysz.krolestwo)
#
# #atrybut klasowy moge zmodyfikowac
#
# Animal.krolestwo = "Flora"
# print(zyrafa.krolestwo)
# print(mysz.krolestwo)
#
# zyrafa.krolestwo = "Fauna"
# print(zyrafa.krolestwo)
# print(mysz.krolestwo)
