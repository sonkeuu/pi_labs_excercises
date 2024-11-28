from threading import Semaphore
import time

sem_a = Semaphore(2)
sem_b = Semaphore(0)
sem_c = Semaphore(0)


def print_a():
    sem_a.acquire()
    print("A")
    time.sleep(0.5)
    sem_b.release()


def print_b():
    print_a()
    print_a()
    sem_b.acquire()
    sem_b.acquire()
    print("B")
    time.sleep(0.5)
    sem_c.release()
    print_c()
    sem_c.release()
    print_c()



def print_c():
    sem_c.acquire()
    print("C")
    time.sleep(0.5)
    sem_a.release()


def start_the_sequence():
    while True:
        print_b()
        #print_c()
        #print_a()


start_the_sequence()



