
def promptKeyword(keyword):
    count = 0
    do = True
    while do:
        userInput = input('Por favor ingresa la palabra clave para terminar: ')
        if(userInput.lower() == keyword): 
            return 'Has ingresado la clave correcta'
        count += 1
        if(count >= 3): 
            do = False
    return 'Has superado el número máximo de intentos'

print(promptKeyword('padawan'))

