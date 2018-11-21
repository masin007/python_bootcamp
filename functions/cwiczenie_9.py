from time import time

def czas(func):
    def wrapper(*args, **kwargs):
        przed_wywolaniem = time()
        wynik = func(*args, **kwargs)
        po_wywolaniu = time()
        print(f"czas wywolania funkcji {func.__name__} {po_wywolaniu - przed_wywolaniem}")
        return wynik
    return wrapper

def fib(x):
    if x <= 1:
        return x
    return fib(x-1) + fib(x-2)


@czas
def funcyja(x):
    return fib(x)

print(funcyja(30))