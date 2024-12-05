from threading import Semaphore
import time
import threading

#AABCC
sem_a = Semaphore(2)
sem_b = Semaphore(0)
sem_c = Semaphore(0)
SEM = Semaphore(1)

def print_a():
    while True:
        sem_a.acquire()
        SEM.acquire()
        time.sleep(0.3)
        print("A")
        sem_b.release()
        SEM.release()


def print_b():
    while True:

        sem_b.acquire()
        sem_b.acquire()
        SEM.acquire()
        time.sleep(0.3)
        print("B")
        sem_c.release()
        sem_c.release()
        SEM.release()


def print_c():
    while True:
        sem_c.acquire()
        SEM.acquire()
        time.sleep(0.3)
        print("C")
        sem_a.release()
        SEM.release()


thread1 = threading.Thread(target=print_a)
thread2 = threading.Thread(target=print_b)
thread3 = threading.Thread(target=print_c)

def start_the_sequence():
    thread2.start()
    thread3.start()
    thread1.start()


start_the_sequence()

