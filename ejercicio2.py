import threading
import time
import random
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S',
                    level=logging.INFO)

nombres = ["Juan", "Mariana", "Daniel", "Ezequiel", "Gimena", "Emilce", "Gabiel", "Gabriela", "Lorena", "Agustin",
           "Julieta"]
lock = threading.Lock()


class Mensajero:

    def __init__(self, id):
        self.id = id

    def crear_mensaje(self, msg):
        self.msg = msg

    def obtener_mensaje(self):
        return self.msg


mensajeros = []

for i in range(2):
    mensajeros.append(Mensajero(i))


def Generador():
    global nombres

    while True:
        lock.acquire()
        try:
            mensaje = f'mensaje de {nombres[random.randint(0, 10)]}'
            mensajero = mensajeros.pop(0)
            mensajero.crear_mensaje(mensaje)
            mensajeros.append(mensajero)
            logging.info(f'{mensaje} recibido')
        finally:
            lock.release()
            time.sleep(random.randint(2, 5))


def Procesador():
    while True:

        try:
            if len(mensajeros) > 0:
                mensajero = mensajeros.pop(0)
                logging.info(f'Mensajero-{mensajero.id} recibió un {mensajero.obtener_mensaje()}')
                mensajeros.append(mensajero)
        finally:
            time.sleep(random.randint(1, 2))


G1 = threading.Thread(target=Generador, name="G1")
G2 = threading.Thread(target=Generador, name="G2")
G3 = threading.Thread(target=Generador, name="G3")

P1 = threading.Thread(target=Procesador, name="P1")
P2 = threading.Thread(target=Procesador, name="P2")
P3 = threading.Thread(target=Procesador, name="P3")
P4 = threading.Thread(target=Procesador, name="P4")
P5 = threading.Thread(target=Procesador, name="P5")

G1.start()
G2.start()
G3.start()

P1.start()
P2.start()
P3.start()
P4.start()
P5.start()

G1.join()
G2.join()
G3.join()

P1.join()
P2.join()
P3.join()
P4.join()
P5.join()
