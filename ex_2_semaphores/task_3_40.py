from threading import Semaphore
import threading

global A, B, C
A = 0
B = 0
C = 3

sem_a = Semaphore(1)
sem_b = Semaphore(0)
sem_c = Semaphore(0)
PSEM = Semaphore(0)

stop_thread = False

def thread_1():
    global A, B, C, stop_thread

    sem_a.acquire()
    if stop_thread:
        return
    A = 10
    print("Thread 1 is done.")
    sem_c.release()
    sem_a.acquire()
    if stop_thread:
        return
    B = B + 5
    C = C + A
    print("Thread 1 is done.")



def thread_2():
    global A, B, C, stop_thread

    sem_b.acquire()
    if stop_thread:
        return
    B = B + C
    print("Thread 2 is done.")
    PSEM.release()
    sem_b.acquire()
    if stop_thread:
        return
    A = A + B
    print("Thread 2 is done.")



def thread_3():
    global A, B, C, stop_thread

    sem_c.acquire()
    if stop_thread:
        return
    A = A + A
    C = B + 10
    print("Thread 3 is done.")
    sem_b.release()
    sem_c.acquire()
    if stop_thread:
        return
    B = B + A
    print("Thread 3 is done.")

    '''thread_2()
    thread_2()
    thread_2()
    thread_2()
    thread_1()'''


def thread_4_40():
    global A, B, C, stop_thread

    PSEM.acquire()
    if stop_thread:
        return
    suma: int = A + B + C
    print(suma)
    stop_thread = True

    sem_a.release()
    sem_b.release()
    sem_c.release()
    PSEM.release()


thread1 = threading.Thread(target=thread_1)
thread2 = threading.Thread(target=thread_2)
thread3 = threading.Thread(target=thread_3)
thread4 = threading.Thread(target=thread_4_40)


def start_the_sequence():
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    return


start_the_sequence()


