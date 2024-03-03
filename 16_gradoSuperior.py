
def validateInput(text):
    do = True
    while do:
        userInput = input(text).lower()
        if(userInput == 'si' or userInput == 'no'):
            do = False
    return userInput

def admissionToHigherEducation():
        print("\033c", end='')
        userInput = validateInput('1. ¿Tienes un titulo de bachiller (si o no)? ')
        if(not(userInput == 'si')):
            userInput = validateInput('2. ¿Has superado la prueba de acceso (si o no)? ')
            if(not(userInput == 'si')):
                return 'No puedes acceder a un grado superior, intenta nuevamente superando la prueba de acceso.\n'
        return '¡Felicidades, puedes acceder a un grado superior!\n'
             
print(admissionToHigherEducation())
