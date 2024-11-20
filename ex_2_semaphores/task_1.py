
from threading import Semaphore, Thread
import time

sem_a = Semaphore(1)
sem_b = Semaphore(1)
sem_c = Semaphore(1)


def print_a():
        sem_a.acquire()
        print("A")
        time.sleep(1)
        sem_b.release()


def print_b():
        sem_b.acquire()
        print("B")
        time.sleep(1)
        sem_c.release()


def print_c():
        sem_c.acquire()
        print("C")
        time.sleep(1)
        sem_a.release()


def start_the_sequence():
    while True:
        print_a()
        print_b()
        print_c()


start_the_sequence()
