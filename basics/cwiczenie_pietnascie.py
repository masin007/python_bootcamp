from random import randint

sX = randint(1, 10)
sY = randint(1, 10)

graczX = randint(1, 10)
graczY = randint(1, 10)


i = 0

print(sX, sY)
print (graczX, graczY)

while True:
    odlegloscX = abs(sX - graczX)
    odlegloscY = abs(sY - graczY)
    kroki = odlegloscY + odlegloscX

    ruch = input("Podaj gdzie chcesz isc w - góra, s - dół, a - lewo, d - prawo ")

    i = i + 1
    if ruch == "w":
        graczY = graczY + 1
    elif ruch == "s":
        graczY = graczY - 1
    elif ruch == "d":
        graczX = graczX + 1
    else:
        graczX = graczX - 1

    kroki2 = abs(sX-graczX) + abs(sY - graczY)

    if (graczX < 1 or graczX > 10 or graczY < 1 or graczY > 10):
        print("Wypadłes poza plansze")
        break

    elif kroki2 == 0:
        print (f"Znalazles skarb, polozenie skarbu to : {sX}, {sY}")
        break
    else:
        print(f"Połozenie gracza to X = {graczX} Y = {graczY}")
        if randint(1, 5) < 5:
            if kroki2 < kroki:
                print(f"Jestes blizej, pozostalo Ci {kroki2} krokow")
            else:
                print(f"Jestes dalej, pozostalo Ci {kroki2} krokow")

        print(f"Liczba ruchow to {i}")



