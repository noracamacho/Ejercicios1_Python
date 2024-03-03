# Ordene 5 números de menor a mayor

def sortNumbers(num):
    for i in range(0, len(num) - 1):
        for j in range(0, len(num) - 1):
            if(num[j] > num[j + 1]):
                aux = num[j]
                num[j] = num[j + 1]
                num[j + 1] = aux
    return num

print(sortNumbers([10, 3, 8, 2, 1]))

