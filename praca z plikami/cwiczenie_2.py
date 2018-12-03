import sys
try:
    print(sys.argv[1])
except IndexError:
    print("Zapomniales podac nzawe pliku")



with open(sys.argv[1]) as f: #context manager

    slownik = {}
    for linia in f:
        linia = linia.split(";")
        user = linia[0]
        action = linia[1]
        time = linia[2]
        time = int(time)

        if action == "LOGIN":
            slownik.get[user] =  - time
        if action == "LOGOUT":
            slownik.get[user] =  time

    print(slownik)






