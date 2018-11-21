class Temperatura:
    def __init__(self, x):
        self.wartosc = x

    def __str__(self):
        return f"Termperatura: {self.wartosc} stopni Celcjusza."

    @property
    def wartosc(self):
        print("getter")
        return 2 * self._wartosc

    @wartosc.setter
    def wartosc(self, x):
        print("setter")
        if x < -273:
            raise ValueError("temperatura za niska")

        self._wartosc = x

    # def get_wartosc(self):
    #     return self._wartosc
    # def set_wartosc(self, x:
    #     self._wartosc = x

x = Temperatura(20)
x.wartosc = 100
print(x)
print(x.wartosc)
x.wartosc = -300

