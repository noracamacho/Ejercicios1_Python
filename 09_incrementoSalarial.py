def salaryIncrease(amount):
    increase = 15
    if(amount <= 15000):
        increase = 20
    return [increase, amount + (amount * increase / 100)]

salary = input('Ingrese es salario del empleado: ')
increasedSalary = salaryIncrease(int(salary))
print(f'\nEl incremento salarial será del {increasedSalary[0]}%, quedando un salario actualizado de sala ${increasedSalary[1]}\n')