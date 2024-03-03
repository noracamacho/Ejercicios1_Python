#  Diseñar un algoritmo que pida por teclado tres números; 
#  si el primero es negativo, debe imprimir el producto de 
#  los tres y si no lo es, imprimirá la suma
from functools import reduce
import array as arr

def addOrMultiply(arrayNumbers):
    if(arrayNumbers[0] < 0):
        return reduce((lambda x, y: x * y), arrayNumbers)
    return reduce((lambda x, y: x + y), arrayNumbers)

numbers = arr.array('i')
print('Ingresar tres números para realizar la operación: ')
for i in range(0, 3):
    numbers.append(int(input('Ingresa número: ')))

print('El resultado del producto es' if(numbers[0] < 0) else 'El resultado de la suma es', addOrMultiply(numbers))