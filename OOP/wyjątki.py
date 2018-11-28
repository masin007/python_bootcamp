lista = [1, 2, 3, 4]

try:
    print(lista[5])
    lista.add(5)
except IndexError as e:
    raise IndexError("Probujesz dodac element spoza listy")
except AttributeError as e:
    print("Prawdopodobnie wywolujesz metode ktorej ten obiekt nie ma")
print("aaa")
