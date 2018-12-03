import sys
try:
    print(sys.argv[1])
except IndexError:
    print("Zapomniales podac nzawe pliku")



with open(sys.argv[1]) as f: #context manager
    i = 0
    for linia in f:

        print(i, linia)
        i += 1