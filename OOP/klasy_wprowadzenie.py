# class NaszaKlasa():
#     x = 4
#     y = 2
#
#
#
# obiekt = NaszaKlasa()
# obiekt2 = NaszaKlasa()
#
# obiekt2.x = 134

# print(obiekt.x)
# print(obiekt2.x)

class Osoba():
    

    def __init__(self, imie, nazwisko):
        print("No siema")
        self.imie = imie
        self.nazwisko = nazwisko



    def przedstaw_sie(self):
        print(f"Nazywam sie {self.imie} {self.nazwisko}")

    @staticmethod
    def metoda_statyczna():
        print("Metoda statyczna")


obiekt = Osoba("Adam", "Małysz")
obiekt2 = Osoba("Adam", "Miciewicz")

obiekt2.imie = "Karol"

print(obiekt.imie)
print(obiekt2.imie)

obiekt.tekst = "qwerty"

obiekt.przedstaw_sie()
obiekt2.przedstaw_sie()
Osoba.metoda_statyczna()


