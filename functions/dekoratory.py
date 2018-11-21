




def prosty_dekorator(func):
    def wrapper(*args, **kwargs):
        print("Przed wywolaniem")
        result = func(*args, **kwargs)
        print("Po wywolaniu")
        return result
    return wrapper

@prosty_dekorator
def fun():
    print("Czesc")

# fun = prosty_dekorator(fun)

print("akuku")
fun()

def dwa_wywolania(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        result = func(*args, **kwargs)
        return result
    return wrapper

# fun = dwa_wywolania(fun)
@dwa_wywolania
@prosty_dekorator
def fun():
    print("czesc")


@prosty_dekorator
def silnia(x):
    wynik = 1
    for i in range(1, x + 1):
        wynik *= i
    return wynik

fun()
