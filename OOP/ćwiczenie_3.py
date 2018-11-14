class ElectricCar():

    def __init__(self, max_range):
        self.range = max_range
        self.max_range = max_range


    def drive(self, distance):

        wynik = self.range - distance
        if wynik < 0:
            wynik = self.range
            self.range = 0
            return wynik
        self.range -= distance
        return distance

    def charge(self):
        self.range = self.max_range
        pass

car = ElectricCar(100)
print(car.drive(70))
print(car.drive(50))
