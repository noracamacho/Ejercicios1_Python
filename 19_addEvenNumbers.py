
def addEvenNumbers(number):
    if(number < 1): return 'El número debe ser mayor a 0'
    evenNumber = number if(number % 2 == 0) else number + 1
    result = evenNumber
    numbersString = f'{evenNumber}'
    for count in range(1, number):
        evenNumber += 2
        result += evenNumber
        numbersString += f' + {evenNumber}'
    return f'El total de la suma de los numeros pares es: {numbersString} = {result}'

num = int(input('Ingresa la cantidad de numeros pares que deseas sumar: '))
print(addEvenNumbers(num))