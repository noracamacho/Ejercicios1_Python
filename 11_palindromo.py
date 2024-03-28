
def palindrome(text):
    text = text.lower().replace(" ", "")
    tail = len(text) - 1
    for head in range(0, round((len(text) - 1)/2)):
        if(text[head] != text[tail]):
            return False
        tail -= 1
    return True

frase = input('Ingresa la palabra o frase que deseas evaluar: ')
print(f'La palabra o frase "{frase}"', 'es palindromo' if (palindrome(frase) == True) else 'no es palindromo' )

