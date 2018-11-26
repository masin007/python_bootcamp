
class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def __str__(self):
        return self.imie + " " + self.nazwisko


class Employee(Osoba):
    def __init__(self, imie, nazwisko, stawka):
        super().__init__(imie, nazwisko)
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



class PremiumEmployee(Employee):
    def __init__(self, imie, nazwisko, stawka):
        super().__init__(imie, nazwisko, stawka)
        self.bonus = 0

    def give_bonus(self, kwota):
        self.bonus += kwota
    def pay_salary(self):
        to_pay = super().pay_salary() + self.bonus
        self.bonus = 0
        return to_pay


employee = PremiumEmployee("jan", "kowalski", 100)

employee.register_time(5)
employee.give_bonus(50)
employee.register_time(10)
print(employee.pay_salary())

