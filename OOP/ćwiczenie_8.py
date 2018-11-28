import pytest

class ToManyBills(ValueError):
    pass

class CashMachine:

    def __init__(self):
        self._money = []


    @property
    def is_avaiable(self,):
        if self._money:
            return True
        return False

    def put_money(self, money):
        if len(money) + len(self._money) > 10:
            raise ToManyBills("BLAD: Zbyt duzo banknotow!")
        self._money.extend(money)




    def withdraw_money(self, to_withdraw):
        bills_to_withdraw = []

        if to_withdraw % 10 != 0:
            raise ValueError("BLAD: Kwota powinna byc wielokrotnoscia 10!")

        for bill in sorted(self._money, reverse = True):
          if sum(bills_to_withdraw) + bill <= to_withdraw:
              bills_to_withdraw.append(bill)
        if sum(bills_to_withdraw) != to_withdraw:
            raise ValueError("BLAD: brak wystarczajacej liczby bankontow do wyplaty")
        for bill in bills_to_withdraw:
            self._money.remove(bill)
        return bills_to_withdraw
    @property
    def empty_slots(self):
        return 10 - len(self._money)

    def __str__(self):
        return f"Bankomat zawiera {self.empty_slots} pustych miejsc na banknoty"

def main():
    bankomat = CashMachine()
    while True:
        operacja = input("Podaj typ operacji w - wplata y - wyplata k - zakoncz: ")
        if operacja == 'k':
            print("Dziekujemy za skorzystanie z naszych uslug")
            return
        if operacja == "0123":
            print(bankomat)
        #wplata
        if operacja == 'w':
            banknoty = input("Podaj jakie banknoty wpłacasz - wpisz je rozdzielajac spacją: ")
            banknoty = banknoty.split()
            banknoty = [int(x) for x in banknoty]

            try:
                bankomat.put_money(banknoty)
            except ToManyBills as e:
                banknoty = False
                print(e)


        #wyplata
        if operacja == 'y':
            kwota_do_wyplaty = int(input("Jaką kwotę chcesz wyplacic: "))
            try:
                wyplacone = bankomat.withdraw_money(kwota_do_wyplaty)
            except ValueError as e:
                wyplacone = False
                print(e)
            if wyplacone:
                print(wyplacone)


main()

def test_za_duzo_banknotow():
    cash_machine = CashMachine()
    with pytest.raises(ToManyBills):
        cash_machine.put_money([50, 20, 20, 10, 20, 20, 50])
        cash_machine.put_money([50, 10, 10, 10, 10])

