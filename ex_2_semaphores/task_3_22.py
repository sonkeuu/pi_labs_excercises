from threading import Semaphore
import threading

global A, B, C
A: int = 0
B: int = 0
C: int = 3

sem_a = Semaphore(0)
sem_b = Semaphore(1)
sem_c = Semaphore(0)
SEM = Semaphore(0)

stop_thread = False

def thread_1():
    global A, B, C, stop_thread

    sem_a.acquire()
    if stop_thread:
        return
    A = 10
    print("Thread 1 is done.")
    SEM.release()
    sem_a.acquire()
    if stop_thread:
        return
    B = B + 5
    C = C + A


def thread_2():
    global A, B, C, stop_thread

    for i in range(3):
        sem_b.acquire()
        if stop_thread:
            return
        B = B + C
        A = A + B
        print("Thread 2 is done.")
        sem_b.release()
    sem_a.release()


def thread_3():
    global A
    global B
    global C

    A = A + A
    C = B + 10
    B = B + A
    print("Thread 3 is done.")


def thread_4_22():
    global A, B, C, stop_thread

    SEM.acquire()
    if stop_thread:
        return
    suma: int = A + B + C
    print(suma)
    stop_thread = True

    sem_a.release()
    sem_b.release()
    sem_c.release()
    SEM.release()


thread1 = threading.Thread(target=thread_2)
thread2 = threading.Thread(target=thread_1)
thread3 = threading.Thread(target=thread_4_22)


def start_the_sequence():
    thread1.start()
    thread2.start()
    thread3.start()
    return


start_the_sequence()

