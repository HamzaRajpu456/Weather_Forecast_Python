import time
import threading



def add():

    for x in range(1,4):
        print(f" Addition : {x} + {x} = {x+x}")
        time.sleep(5)

def multiply():

    for x in range(1,4):
        print(f" Multiplication : {x} X {x} = {x*x}")
        time.sleep(2)


def subtract():

    for x in range(1,4):
        print(f" Subtraction : {x} - 1 = {x - 1}")
        time.sleep(3.5)


thread_1 = threading.Thread(target = add)
thread_2 = threading.Thread(target = multiply)
thread_3 = threading.Thread(target = subtract)


thread_1.start()
thread_2.start()
thread_3.start()