x = int(input("Podaj pozycje gracza X: "))
y = int(input("Podaj pozycje gracza Y: "))

if (x < 0) or (x > 100) or (y < 0) or (y > 100):
    pozycja = "poza plansza"
elif x >= 90 and y >=90:
    pozycja = "prawy gorny rog"
elif x<=10 and y>=90:
    pozycja = "lewy gorny rog"
elif x<=10 and y<=10:
    pozycja = "lewy dolny rog"
elif x>=90 and y<=10:
    pozycja = "prawy dolny rog"
elif y<10:
    pozycja = "dolna krawedz"
elif y>90:
    pozycja = "gorna krawedz"
elif x<10:
    pozycja = "lewa krawedz"
elif x>90:
    pozycja = "prawa krawedz"
else:
    pozycja = "centrum"

print(f"Twoja pozycja to : {pozycja}")