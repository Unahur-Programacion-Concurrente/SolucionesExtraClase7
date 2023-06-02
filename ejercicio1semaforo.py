import threading
import time
import random
import logging

energia = 0
sem = threading.Semaphore(2)
lock = threading.Lock()

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S',
                    level=logging.INFO)

def generador():
    global energia

    while True:
        lock.acquire()
        try:
            energia += 1
        finally:
            lock.release()
            time.sleep(random.randint(1, 2) / 100)


def medidor():
    global energia, num_medidores

    while True:
            valor0 = 0
            valor1 = 0
            sem.acquire()
            lock.acquire()
            try:
                valor0 = energia
                logging.info(f'{threading.current_thread().name} esta midiendo')
            finally:
                lock.release()
                time.sleep(1)
            lock.acquire()
            try:
                valor1 = energia
                logging.info(f'La potencia generada es {valor1 - valor0} Kw')
            finally:
                lock.release()
                sem.release()
            
            time.sleep(random.randint(5,15))

hilos = []

for k in range(2):
    hilos.append(threading.Thread(target=generador, name=f'Generador {k}'))

for k in range(10):
    hilos.append(threading.Thread(target=medidor, name=f'Medidor {k}'))

for hilo in hilos:
    hilo.start()

