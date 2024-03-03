# Reciba un año y te responda si es o no es bisiesto.

def isLeapYear(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

year = int(input('\nIngresa el año que deseas evaluar: '))
print(f'El año {year} es año bisiesto.\n' if isLeapYear(year) else f'El año {year} no es año bisiesto.\n' )
