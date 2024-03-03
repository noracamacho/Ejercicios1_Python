# Lea el nombre de la persona y lo imprima en la pantalla

def printName(firstName, lastName):
    print(f'\nBienvenido {firstName} {lastName}.\n')

name = input('\nEnter your firstname: ')
lName = input('\nEnter your lastname: ')

printName(name, lName)