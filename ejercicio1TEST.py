import threading
import time
import random

contador = 0

def funcion():
    global contador
    for i in range(100000):
        contador = contador + 1

print("Inicio programa principal")
print("Valor Inicial: " + str(contador))

thread_1=threading.Thread(target=funcion)
thread_2=threading.Thread(target=funcion)
thread_3=threading.Thread(target=funcion)
thread_4=threading.Thread(target=funcion)
thread_5=threading.Thread(target=funcion)
thread_6=threading.Thread(target=funcion)

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()
thread_5.start()
thread_6.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()
thread_5.join()
thread_6.join()

print("Valor Final: " + str(contador))
