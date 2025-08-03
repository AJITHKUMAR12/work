import threading
from threading import *
def show():
    print("this is the child thread")
t=Thread(target=show())
t.start()
print("this is the parent thread")

class myThread(Thread):
    def run(self):
        for i in range(3):
            print("\n this is the child thread1")
t=myThread()
t.start()
for i in range(3):
    print("\n this is the parent thread1")




class Demo:
    def run(self):
        for i in range(3):
            print("\n this is the child thread2")
obj=Demo()
t=Thread(obj.run())
t.start()
for i in range(3):
    print("\n this is the parent thread2")