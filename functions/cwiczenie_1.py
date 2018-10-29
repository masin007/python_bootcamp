

def czy_pierwsza(liczba):

    for i in range(2, liczba - 1):
        if liczba % i == 0:
            return False

    return True








def test_czy_jest_pierwsza_dla_liczby_pierwszej():
    assert czy_pierwsza(11)
    assert czy_pierwsza(3)
    assert czy_pierwsza(101)



def test_czy_jest_pierwsza_dla_liczby_nie_pierwszej():
    assert not czy_pierwsza(10)
    assert not czy_pierwsza(27)
    assert not czy_pierwsza(121)