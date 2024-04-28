
import math
# Calcule el volumen de una esfera

def calculateVolume(radio):
    return 4/3 * math.pi * math.pow(radio, 3)

radio = int(input('Ingresa el radio de la esfera: '))

print(f'El volumen de la esfera con radio {radio} es {round(calculateVolume(radio), 2)} cm\xB3')

# -------------

# def calculateVolumePrint(radio):
#     print(4/3 * math.pi * radio ** 3)

# calculateVolumePrint(2)

