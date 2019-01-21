# liczba = 0
# for i in range(500000):
#     tmp = liczba
#     tmp += 1
#     liczba = tmp
# print(liczba)

from threading import Thread
from time import sleep

class MyThread(Thread):
    def __init__(self):
        super().__init__()
        pass
    def run(self):
        sleep(4)
        print("Cześć")


watek = MyThread()
watek.start()

print("Hej")
watek.join()