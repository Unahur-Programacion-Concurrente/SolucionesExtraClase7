import threading
import time
import random
import logging

energia = 0
num_medidores = 0

lock = threading.Lock()
no_maximo = threading.Condition(lock)

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
            no_maximo.acquire()
         #   logging.info(f'lock adquirido {lock.locked()}')
            try:
                while num_medidores == 2:
                    no_maximo.wait()
                num_medidores += 1
                valor0 = energia
                logging.info(f'{threading.current_thread().name} esta midiendo')
            finally:
                no_maximo.release()
                time.sleep(1)
            no_maximo.acquire()
            try:
                valor1 = energia
                logging.info(f'La potencia generada es {valor1 - valor0} Kw')
                num_medidores -=1
            finally:
                no_maximo.notify()
                no_maximo.release()
            
            time.sleep(random.randint(1,5))

hilos = []

for k in range(2):
    hilos.append(threading.Thread(target=generador, name=f'Generador {k}'))

for k in range(10):
    hilos.append(threading.Thread(target=medidor, name=f'Medidor {k}'))

for hilo in hilos:
    hilo.start()

