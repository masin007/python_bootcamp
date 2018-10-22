
liczby = [5, 2, 1, 4, 3]

min_ = None
max_ = None

min_ = liczby[0]
max_ = liczby[0]
for liczba in liczby:
    if liczba < min_:
        min_ = liczba
    if liczba > max_:
        max_ = liczba

print("Wartości", min_, max_)
print("Indeksy, czyli pozycje", liczby.index(min_), liczby.index(max_))


# liczby[liczby.index(min_)] = max_
# liczby[liczby.index(max_)] = min_

liczby[liczby.index(min_)], liczby[liczby.index(max_)] = max_, min_
assert liczby == [1, 2, 5, 4, 3]

print(liczby)

# for i in range(len(liczby)):
#     print(liczby[i])
