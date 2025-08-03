from threading import *
import time
class demo:
    def num(self):
        for i in range(1,5):
            print("the number is",i)
            time.sleep(1)
    def sum(self):
        for i in range(1,5):
            print("sum of number is",i+i)
            time.sleep(1)
    def square(self):
        for i in range(1,5):
            print("square of number is",i*i)
            time.sleep(1)

ob=demo()
t=Thread(target=ob.num())
t.start()
time.sleep(0.2)
t1=Thread(target=ob.sum())
t1.start()
time.sleep(0.2)
t2=Thread(target=ob.square())
t2.start()
t.join()
t1.join()
t2.join()
for i in range(1,5):
    print("this is the main thread")
