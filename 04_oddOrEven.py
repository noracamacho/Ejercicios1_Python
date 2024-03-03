# Te diga si un número es par o impar

def isEven(number):
    return number % 2 == 0

num = input('Ingresa un múmero: ')
print(num, 'is even' if isEven(int(num)) == True else 'is odd')

