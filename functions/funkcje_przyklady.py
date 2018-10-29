# def hello():
#     print("Hello World!")
#     return 10
#
# print(type(hello))
#
# hello()
#
# def hello2(name):
#     print(f"Hello {name}")
#
# hello2("world")
#
#
# def hello3(name="World"):
#     print(f"Hello {name}")
#
# hello3()
# hello3("Marcin")
#
#
# x = print("testuje co zwraca print")
# print("x:", x)
#
# y = dir()
# print("y:", y)
#
# z = hello()
# print("z: ", z)

def dodaj(a, b):
    return a + b

def test_dodaj_dwie_liczby():
    assert dodaj(1 ,2) == 3

def test_dodaj_dwa_napisy():
    assert dodaj("1", "2") == "12"




# wynik = dodaj(1 ,2)
# wynik2 = dodaj(1.1, 3.3)
# print(wynik, wynik2)



