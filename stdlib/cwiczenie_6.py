from threading import Thread
from urllib.request import urlopen
from time import time


class MyThread(Thread):

    def run(self):
        with urlopen("https://www.wp.pl") as plik:
            print(plik.read())

przed = time()

watki = []

for i in range(10):
    watek = MyThread()
    watek.start()
    watki.append(watek)

for watek in watki:
    watek.join()


po = time()
print(po-przed)
