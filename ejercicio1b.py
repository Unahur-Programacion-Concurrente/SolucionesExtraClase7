import threading
import time
import random
import logging

energia = 0
num_medidores = 0

lock = threading.Lock()
no_maximo = threading.Condition()

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S',
                    level=logging.INFO)

def generador():
    global energia

    while True:
        no_maximo.acquire()
        try:
            energia += 1
        finally:
            no_maximo.release()
            time.sleep(random.randint(1, 2) / 100)


def medidor():
    global energia, num_medidores

    while True:
            valor0 = 0
            valor1 = 0
            no_maximo.acquire()
            try:
                if num_medidores < 2:
                    valor0 = energia
                    num_medidores += 1
                    logging.info(f'{threading.current_thread().name} esta midiendo')
                else:
                    continue
            finally:
                no_maximo.release()
            time.sleep(1)
            no_maximo.acquire()
            try:
                valor1 = energia
                num_medidores -=1
            finally:
                no_maximo.release()
            logging.info(f'La potencia generada es {valor1 - valor0} Kw')
            time.sleep(random.randint(1,5))

hilos = []

for k in range(2):
    hilos.append(threading.Thread(target=generador, name=f'Generador {k}'))

for k in range(10):
    hilos.append(threading.Thread(target=medidor, name=f'Medidor {k}'))

for hilo in hilos:
    hilo.start()

