from threading import Semaphore
import time

sem_a = Semaphore(2)
sem_b = Semaphore(0)
sem_c = Semaphore(0)

global A
global B
global C

A = 0
B = 0
C = 3

def thread_1():
    A = 10
    B = B + 5
    sem_a.acquire()
    C = C + A


def thread_2():
    B = B + C
    sem_b.acquire()
    A = A + B


def thread_3():
    A = 2*A
    C = B + 10
    sem_c.acquire()
    B = B + A


def thread_4():
    ...

def start_the_sequence():
    while True:
        thread_1()
        thread_2()
        thread_3()
        thread_4()


start_the_sequence()



