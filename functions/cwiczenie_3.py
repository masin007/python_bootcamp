




def test_policz_znaki_bez_znacznikow():
    assert policz_znaki("ala ma kota a kot ma ale") == 0

def test_policz_znaki_jeden_poziom_zaglebienia_standardowe_znaczniki():
    assert policz_znaki("ala ma <kota> a kot ma ale", "[", "]") == 4

def test_policz_znaki_wiele_poziomow_zaglebienia_niestandardowe_znaczniki():
    assert policz_znaki("ala ma [kota [a kot]] ma [ale]") == 18
    assert policz_znaki("ala ma [kota [a kot]] ma [ale]", start = "[", end = "]") == 18

