from functools import reduce

print('Ingresar números enteros para determinar el maximo, el minimo y el promedio,\ncuando ya no desees ingrear más números, ingresa el número 0')
arrNumbers = []
do = True
while do:
    userInput = int(input('Ingresa número: '))
    if(userInput != 0): 
        arrNumbers.append(userInput)
    else:
        do = False
    
maxNumber = max(arrNumbers)
minNumber = min(arrNumbers)
sum = reduce((lambda x, y: x + y), arrNumbers)
avg = sum / len(arrNumbers)
print('los números ingresados son', *arrNumbers, sep = ', ')
print(f'Max: {maxNumber} Min: {minNumber} Suma: {sum} Promedio: {avg}\n')
