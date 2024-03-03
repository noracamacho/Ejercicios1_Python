
def palindrome(text):
    tail = len(text) - 1
    count = 0
    for head in range(0, len(text) - 1):
        if(text[head] != text[tail]):
            count += 1
        tail -= 1
    if(count == 0): 
        print('La palabra o frase', text, 'es palindromo')
    else:
        print('La palabra o frase', text, 'no es palindromo')

palindrome('aronnoras')

