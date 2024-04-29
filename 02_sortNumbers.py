# Ordene 5 números de menor a mayor

def isFloat(element):
    if element % 1 == 0:
        return int(element)
    return element

def sortNumbers(numbers):
    numbers.sort()
    return list(map(isFloat, numbers))

inputNumbers = []
for num in range(0, 5):
    usr = float(input('Ingresa un número: '))
    inputNumbers.append(usr)

print(sortNumbers(inputNumbers))




# def sortNumbers(num):
#     # for i in range(0, len(num) - 1):
#     #     for j in range(0, len(num) - 1):
#     #         if(num[j] > num[j + 1]):
#     #             aux = num[j]
#     #             num[j] = num[j + 1]
#     #             num[j + 1] = aux
#     return num