produkty = {
    "pomidory": 5,
    "ziemniak": 2,
    "ogorki": 4,
    "cebula": 1,
    "gruszki": 7,
    "jajka": 11,
    "kalafior": 9,
}
print("W naszym sklepie oferujemy")
rachunek = 0
koszyk = {}
magazyn = {
    "pomidory": 10,
    "ziemniak": 10,
    "ogorki": 10,
    "cebula": 10,
    "gruszki": 10,
    "jajka": 10,
    "kalafior": 10,
}

while True:
    komenda = input(""" Wybierz opcje:
    [d] - dodaj do magazynu
    [k] - kup
    [z] - zakoncz
    """)

    if komenda == "k":
        print("w naszym sklepie oferujemy: ")
        for produkt in produkty:
            print(f" - {produkt} - w cenie: {produkty[produkt]} PLN")

        print()

        wybor_produktu = input("Ktory produkt chcesz kupic? Jeżeli konczysz zakupy wpisz koniec ")
        if wybor_produktu == "koniec":
            break
        if wybor_produktu in produkty:
            ile = int(input(f"Ile chcesz kupic [{wybor_produktu}]"))
            if ile <= magazyn[wybor_produktu]:
                koszyk[wybor_produktu] = ile
                magazyn[wybor_produktu] = magazyn[wybor_produktu] - ile
                rachunek = rachunek + ile * produkty[wybor_produktu]
            else:
                print (f"Nie mam tyle produktu! Pozostalo {magazyn[wybor_produktu]}")
        else:
            print("Sorry nie ma takiego produktu")
        print()
        print("-" * 40)
    elif komenda == "d":
        co = input("jaki produk chcesz dodac ")
        ile = int(input(f"Ile {co} chcesz dodac do koszyka"))
        magazyn[co] = magazyn.get(co, 0) + ile
        if co not in produkty:
            cena = float(input (f"Jaka cena za {co}"))
            produkty[co] = cena
    elif komenda == "z":
        break


    print("Twoj koszyk zakupowy to:")
    print(koszyk)
    print(f"Twoj rachunek to: {rachunek} ")
    print("Dziekujemy, zapraszamy ponownie!")



