class Iterator:

    def __init__(self, wartosc):
        self.wartosc = wartosc

    def __iter__(self):
         self.licznik = 0
         return self

    def __next__(self):

        if self.licznik  >  self.wartosc:
            raise StopIteration
        liczba = self.licznik
        self.licznik += 1
        return liczba

for i in Iterator(50):
    print(i)