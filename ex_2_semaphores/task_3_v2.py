from threading import Semaphore

# to do:
# sum = 40
# sum = 22


sem_a = Semaphore()
sem_b = Semaphore()
sem_c = Semaphore()
PSEM = Semaphore(1)

def thread_1():
    global A
    global B
    global C

    PSEM.acquire()
    A = 10
    B = B + 5
    #sem_a.acquire()
    C = C + A
    print("Thread 1 is done.")
    PSEM.release()


def thread_2():
    global A
    global B
    global C
    A = 0
    B = 0
    C = 3

    PSEM.acquire()
    B = B + C
    #sem_b.acquire()
    A = A + B
    print("Thread 2 is done.")
    PSEM.release(1)


def thread_3():
    global A
    global B
    global C

    PSEM.acquire()
    A = A + A
    C = B + 10
    #sem_c.acquire()
    B = B + A
    print("Thread 3 is done.")
    PSEM.release(1)


def thread_4():
    global A
    global B
    global C

    thread_2()
    thread_2()
    thread_3()
    PSEM.acquire()
    suma: int = A + B + C
    print(suma)
    #PSEM.release()

def start_the_sequence():
    while True:
        thread_4()


start_the_sequence()