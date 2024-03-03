
def invertedSteps(numOfSteps):
    for step in range(0, numOfSteps + 1):
        row = ' ' * step + '*' * (numOfSteps - step)
        print(row)

steps = int(input('Ingresa el número de escalones que deseas tenga la escalera invertida: '))
invertedSteps(steps)