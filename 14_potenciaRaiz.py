
from math import sqrt

def potenciaRaiz():
    number = int(input('Ingresa un número para ralizar el cálculo: '))
    print(f'Error: El numero deber ser mayor a 0\n' if number <= 0 else f'Su cuadrado es {number ** 2} y su raiz es {sqrt(number)}')

potenciaRaiz()
