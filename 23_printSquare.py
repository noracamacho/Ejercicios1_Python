
def topBottom(side,bottom = False):
    row = '\n' + '* ' * side + ('\n' if(bottom == True) else '')
    return row

def lats(side):
    rows = ''
    if(side - 2 > 0): rows += (('\n*' + '  ' * (side - 2) + ' *') * (side - 2))
    return rows

def createSquare(num):
    if(num < 2): return 'El cuadrado debe contener al menos 2 caracteres por lado.\n'
    square = topBottom(num)
    square += lats(num)
    square += topBottom(num, True)
    return square

side = int(input('Ingresa el numero de caracteres que deseas que tenga de lado el cuadrado: '))
print(createSquare(side))