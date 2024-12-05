from threading import Semaphore
import time
import threading

#CBAB
sem_a = Semaphore(1)
sem_b = Semaphore(0)
sem_c = Semaphore(2)
SEM = Semaphore(1)

def print_a():
    while True:
        sem_a.acquire()
        sem_a.acquire()
        #SEM.acquire()
        print("A")
        time.sleep(0.3)
        sem_b.release()
        #SEM.release()


def print_b():
    while True:
        sem_b.acquire()
        #SEM.acquire()
        print("B")
        time.sleep(0.3)
        sem_a.release()
        sem_c.release()
        #SEM.release()


def print_c():
    while True:
        sem_c.acquire()
        sem_c.acquire()
        #SEM.acquire()
        print("C")
        time.sleep(0.3)
        sem_b.release()
        #SEM.release()


thread1 = threading.Thread(target=print_a)
thread2 = threading.Thread(target=print_b)
thread3 = threading.Thread(target=print_c)

def start_the_sequence():
    thread2.start()
    thread3.start()
    thread1.start()


start_the_sequence()



