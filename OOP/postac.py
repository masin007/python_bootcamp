from random import randint
from Przedmiot import Przedmiot

class Postac:
    def __init__(self, imie, atak, zdrowie):
        self.imie = imie
        self._atak = atak
        self.zdrowie = zdrowie
        self.max_zdrowie = zdrowie
        self.ekwipunek = []

    @property
    def atak(self):
        atak_xtra = self._atak
        for przedmiot in self.ekwipunek:
            atak_xtra += przedmiot.bonus_atk
        return atak_xtra

    def otrzymaj_obrazenia(self, obrazenia):
        # print(f"{self.imie} oberwal {obrazenia} obrazen.")
        self.zdrowie = self.zdrowie - obrazenia
        if self.zdrowie < 0:
            self.zdrowie = 0

    def wylecz(self, punkty):
        if self.czy_zyje():
            # print(f"{self.imie} wyleczyl sie za {punkty} punktow.")
            self.zdrowie = self.zdrowie + punkty
            if self.zdrowie > self.max_zdrowie:
                self.zdrowie = self.max_zdrowie
        else:
            print(f"Probujesz wyleczyc trupa")

    def czy_zyje(self):
        return self.zdrowie > 0

    def moc_ataku(self):
        moc = randint(self.atak//2, self.atak)
        return moc

    def __str__(self):
        if self.czy_zyje():
            napis = "EKWIPUNEK:\n"
            for x in self.ekwipunek:
                napis += str(x) + "\n"

            return f"Jestem {self.imie}, mam {self.atak} ataku i {self.zdrowie}/{self.max_zdrowie} życia.\n" + napis
        else:
            return f"Jestem {self.imie}, mam {self.atak} ataku i nie żyję."

    def daj_przedmiot(self, przedmiot):
        self.ekwipunek.append(przedmiot)



    @staticmethod
    def walka(atakujacy, broniacy):
        print(f"Walka: {atakujacy.imie} vs {broniacy.imie}")
        while atakujacy.czy_zyje() and broniacy.czy_zyje():
            print(atakujacy)
            print(broniacy)
            atak_atakujacego = atakujacy.moc_ataku()
            atak_broniacego = broniacy.moc_ataku()
            broniacy.otrzymaj_obrazenia(atakujacy.atak)
            print(f"{atakujacy.imie} udrza {broniacy.imie} za {atak_atakujacego} obrażeń")
            atakujacy.otrzymaj_obrazenia(broniacy.atak)
            print(f"{broniacy.imie} udrza {atakujacy.imie} za {atak_broniacego} obrażeń")
        print("KONIEC WALKI")

rufus = Postac("Rufus", 30, 100)
# rufus.przedstaw_sie()
#
# rufus.otrzymaj_obrazenia(20)
#
# rufus.otrzymaj_obrazenia(90)
#
# print(rufus.czy_zyje())
# rufus.wylecz(70)
# print(rufus)


janusz = Postac("Janusz", 40, 800)

tulipan = Przedmiot("Zielony tulipan zniszczenia", 5)
rufus.daj_przedmiot(tulipan)



Postac.walka(rufus, janusz)
print(rufus)
print(janusz)

print(f"bonus.atk: {rufus.atak()}")

# def test_nowa_postac():
#     postac = Postac("Albert", 1, 20)
#     assert postac.imie == "Albert" and postac.atak == 1 and postac.zdrowie == 20 and postac.max_zdrowie == 20
#
# def test_obrazenia():
#     postac = Postac("Rafal", 5, 200)
#     assert postac.zdrowie ==200
#     postac.otrzymaj_obrazenia(80)
#     assert postac.zdrowie == 120
#     postac.otrzymaj_obrazenia(200)
#     assert postac.zdrowie == 0
#
# def test_leczenie():
#     postac = Postac("Rafal", 5, 200)
#     postac.otrzymaj_obrazenia(80)
#     assert postac.zdrowie == 120
#     postac.wylecz(50)
#     assert postac.zdrowie == 170
#
# def test_leczenie_nieboszczyka():
#     postac = Postac("Rafal", 5, 200)
#     postac.otrzymaj_obrazenia(800)
#     assert postac.zdrowie == 0
#     postac.wylecz(50)
#     assert postac.zdrowie == 0
#
# def test_za_duze_leczenie():
#     postac = Postac("Rafal", 5, 200)
#     postac.otrzymaj_obrazenia(80)
#     assert postac.zdrowie == 120
#     postac.wylecz(500)
#     assert postac.zdrowie == 200
#
