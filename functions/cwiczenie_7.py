# lista = [1, 2, 3, 4, 5, 6]
#
# out = [False, False, False, True, True, True]
#
# def bigger_than_3(liczba):
#     if liczba > 3:
#         return True
#     return False
#
# def smaller_than_3(liczba):
#     if liczba < 3:
#         return True
#     return False
#
# def sprawdzam_czy_wieksze_niz_3(lista):
#     out = []
#     for element in lista:
#         # if element > 3:
#         #     out.append(True)
#         # else:
#         #     out.append(False)
#     out.append(bigger_than_3(element))
#     return out
#
# def sprawdzam_czy(lista, warunek):
#     """
#
#     :param lista: - lista wejsciowa
#     :param warunek: - jakis przepis, funkcja jaki jest ten warunek
#     :return:
#     """
#
#
# x = lambda i:i == 4
#
#
#
# assert sprawdzam_czy_wieksze_niz_3(lista) == out

def przytnij(lista, start, stop):
    result = []
    dodawac_do_listy = False
    for element in lista:
        if start(element):
            dodawac_do_listy = True
        if dodawac_do_listy:
            result.append(element)
        if stop(element):
            break

def test_przytnij():
    assert przytnij(
        lista=[1, 2, 3, 4, 5, 6, 7],
        start=lambda x: x > 3,
        stop=lambda x: x == 6,
    ) == [4, 5, 6]
