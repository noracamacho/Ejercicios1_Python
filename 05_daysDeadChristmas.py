import datetime

currentDate = datetime.datetime.now()
currentYear = currentDate.year

def daysCalculator(startMonth, startDay, endMonth, enDay, holiday):
    elapsedDays = calculateElapsedDays(startMonth, startDay, endMonth, enDay)
    print(f'Han pasado {-elapsedDays} día(s) desde {holiday}' if(elapsedDays < 0) else f'Faltan {elapsedDays} día(s) para {holiday}')

def calculateElapsedDays(monthInitial, dayInitial, monthFinal, dayFinal):
    calendarMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    elapsedDays = 0
    isPastDate = False
    # Verify if the date given by user is past the holiday
    if(monthInitial > monthFinal):
        monthInitial, monthFinal = monthFinal, monthInitial
        dayInitial, dayFinal = dayFinal, dayInitial
        isPastDate = True
    
    for month in range(monthInitial, monthFinal):
        elapsedDays += calendarMonths[month]
    # if(isPastDate): return -(elapsedDays + dayFinal - dayInitial)
    return  -(elapsedDays + dayFinal - dayInitial) if(isPastDate) else (elapsedDays + dayFinal - dayInitial)

def menuSelection():
    optionMenu = ''
    month = 0
    day = 0
    do = True

    while do:
        print('1 - Obtener el cálculo de los día con fecha actual (1)')
        print('2 - Obtener el cálculo de los día ingresando fecha (2)')
        print('3 - Terminar (3)')
        optionMenu = input('Opcion: ')

        match optionMenu:
            case '1':
                month = currentDate.month
                day = currentDate.day
                daysCalculator(month - 1, day, 10, 2, 'Día de Muertos')
                daysCalculator(month - 1, day, 11, 25, 'Navidad')
            case '2':
                month = int(input('Ingresa mes MM: '))
                day = int(input('Ingresa día DD: '))
                daysCalculator(month - 1, day, 10, 2, 'Día de Muertos')
                daysCalculator(month - 1, day, 11, 25, 'Navidad')
            case '3':
                return 'Gracias'
            case _:
                print('Elige la opción correcta')
            
        if(optionMenu != '3'): 
            wait = input('\nPresiona cualquir tecla para continuar')

menuSelection()