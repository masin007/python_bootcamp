napis = "koszt $cena PLN"
napis2 = "kwota $cena brutto"

def formatuj(*args, **kwargs):
    tekst ="\n".join(args)
    for k in kwargs:
        tekst = tekst.replace("$"+k, str(kwargs[k]))
    return tekst


print(formatuj(napis,napis2, cena="10"))


def test_formatuj():
    assert formatuj(
        "koszt $cena PLN",
        "kwota $cena brutto",
        cena=10,
    ) == "koszt 10 PLN\nkwota 10 brutto"