# Otworzenie pliku do odczytu
with open("dane/input.txt") as f:   #context manager
    for linia in f:
        if len(linia) > 600:
            print(len(linia))


# tryb do odczytu

with open("info.txt", "w", encoding="utf8") as f:
    for i in range(10):
        f.write("Jakis tekst\n")


# with open("info.txt", "a", encoding="utf8") as f:
#     f.write("Inny tekst")

