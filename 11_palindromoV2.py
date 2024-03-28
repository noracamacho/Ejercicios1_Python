# Valide si una palabra o frase es palíndromo.
    #reversedText = "".join(reversed(text))

def palindromo(text):
    text = text.replace(" ", "").lower()
    if text == "".join(reversed(text)):
        return True
    return False

usersInput = input('Enter the text you want to validate: ')
print(usersInput, 'es palindromo' if palindromo(usersInput) else 'no es palindromo')
