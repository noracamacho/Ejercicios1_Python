
def addNumbers(num):
    for i in range(1, num):
        num += i
    return num

number = int(input('Ingresa la cantidad de numeros que deseas sumar: '))
print(f'El total de la suma es: {addNumbers(number)}')