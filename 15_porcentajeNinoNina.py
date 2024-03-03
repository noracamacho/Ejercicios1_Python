
def porcentage(cuantity1, cuantity2):
    return cuantity1 * 100 / (cuantity1 + cuantity2)

def porcentageBoysGirls():
    numBoys = int(input('Ingresa la cantidad de niños en el colegio: '))
    numGirls = int(input('Ingresa la cantidad de niñas en el colegio: '))
    print(f'\n{porcentage(numBoys, numGirls)}% de los alumnos son niños')
    print(f'{porcentage(numGirls, numBoys)}% de los alumnos son niñas\n')

porcentageBoysGirls()
