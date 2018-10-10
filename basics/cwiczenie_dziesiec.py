pierwsza_liczba = input("Podaj pierwsza liczbe: ")
druga_liczba = input("Podaj druga liczbe: ")
operator = str(input("Podaj operator: "))

if pierwsza_liczba.isnumeric() and druga_liczba.isnumeric():
    pierwsza_liczba = int(pierwsza_liczba)
    druga_liczba = int(druga_liczba)
    if operator == "+":
       wynik = pierwsza_liczba + druga_liczba
    elif operator == "-":
        wynik = pierwsza_liczba - druga_liczba
    elif operator == "*":
        wynik = pierwsza_liczba * druga_liczba
    elif operator == "/":
        if druga_liczba != 0:
            wynik = pierwsza_liczba / druga_liczba
        else:
            wynik = "nie mozna dzielic przez 0"

    else:
        print("Niepoprawny operator")

    print(f"Wynik operacji wyniosl: {wynik}")
else:

    print("Argumenty powinny byc liczbami")