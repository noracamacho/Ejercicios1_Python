# Calcule el área de un triangulo

def triangleArea(base, height):
    return base * height / 2

base = int(input('\nIngresa la altura (cm): '))
height = int(input('Ingresa la base (cm): '))
print(f'El área de triángulo es {triangleArea(base, height)} cm\xB2\n')
