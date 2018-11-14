class Product:
    def __init__(self, cena, nazwa, id):
        self.cena = cena
        self.nazwa = nazwa
        self.id = id
    def print_info(self):
        print(f"{self.cena} {self.nazwa} {self.id}")


produkt = Product(1, "woda", "dupa")

produkt.print_info()

print(produkt.nazwa)