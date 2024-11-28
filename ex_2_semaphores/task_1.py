from threading import Semaphore
import time

sem_a = Semaphore(0)
sem_b = Semaphore(0)
sem_c = Semaphore(1)


def print_a():
    sem_a.acquire()
    print("A")
    time.sleep(0.5)
    sem_b.release()


def print_b():
    print_c()
    sem_b.acquire()
    print("B")
    time.sleep(0.5)
    sem_a.release()
    print_a()
    sem_b.acquire()
    print("B")
    time.sleep(0.5)
    sem_c.release()



def print_c():
    sem_c.acquire()
    print("C")
    time.sleep(0.5)
    sem_b.release()


def start_the_sequence():
    while True:
        print_b()
        #print_c()
        #print_a()


start_the_sequence()



