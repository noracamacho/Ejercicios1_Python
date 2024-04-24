
def topBottom(side, bottom = False):
    return '\n' + '* ' * side + ('\n' if(bottom == True) else '')

def lats(side):
    return (('\n*' + '  ' * (side - 2) + ' *') * (side - 2))

def createSquare(num):
    if(num < 2): 
        return 'El cuadrado debe contener al menos 2 caracteres por lado.\n'
    return topBottom(num) + lats(num) + topBottom(num, True)

side = int(input('Ingresa el numero de caracteres que deseas que tenga de lado el cuadrado: '))
print(createSquare(side))