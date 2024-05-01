from threading import Semaphore, Thread
import time

sem: Semaphore = Semaphore()
stop_thread = False
def fun1():
    while True:
        global stop_thread
        if stop_thread:
            break
        sem.acquire()
        print(1)
        sem.release()
        time.sleep(0.25)


def fun2():
    while True:
        global stop_thread
        if stop_thread:
            break
        sem.acquire()
        print(2)
        sem.release()
        time.sleep(0.25)


t1: Thread = Thread(target=fun1)
t2: Thread = Thread(target=fun2)
try:
    t1.start()
    t2.start()
    while True:
        1 + 1
except KeyboardInterrupt:
    print('\nReceived keyboard interrupt, quitting threads.')
    stop_thread = True
    t1.join()
    print('Thread 1 stopped!')
    t2.join()
    print('Thread 2 stopped!')
    exit(1)
