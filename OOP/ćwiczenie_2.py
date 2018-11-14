class Employee:
    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.godzin = 0

    def register_time(self, godzin):

        self.godzin += godzin
        if godzin > 8:
            self.godzin += godzin -8

    def pay_salary(self):
        wyplata = self.godzin * self.stawka
        self.godzin = 0
        return wyplata



employee = Employee("jan", "kowalski", 100)

employee.register_time(5)
employee.register_time(10)

print(employee.pay_salary())

