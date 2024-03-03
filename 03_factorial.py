
def factorial(num):
    if(num < 1):
        return 1
    return num * factorial(num - 1)

do = True
while do:
    number = input('\nEnter the number you want to calculate: ')
    number = int(number)
    if number > 0:
        print(f'El factorial de {number} es {factorial(number)}\n')
        do = False