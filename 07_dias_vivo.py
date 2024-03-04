import datetime


def calculateElapsedDays(day, month, year):
    calendarMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    month -= 1
    elapsedDays = 0
    for i in range(0, month):
        elapsedDays += calendarMonths[i]
    
    # Comprobar si el año es bisiesto y si la fecha dada es despues del 28 de febrero
    if((month > 1 or (month == 1 and day > 28)) and isLeapYear(year)):
        elapsedDays += 1

    return elapsedDays + day

# Funcion para verificar si un año es bisiesto
def isLeapYear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def daysLived():
    totalDays = 0
    currentDate = datetime.datetime.now()
    currentDay = currentDate.day
    currentMonth = currentDate.month
    currentYear = currentDate.year
    monthCalendar = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio' ,'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    birthYear = int(input('Ingresar año de nacimiento YYYY: '))
    birthMonth = int(input('Ingresar mes de nacimiento MM: '))
    birthDay = int(input('Ingresar día de nacimiento DD: '))

    # ** Dias acumulados en los años completos entre el año siguiente al año de nacimiento y el año actual
    for year in range(birthYear + 1, currentYear):
        if(isLeapYear(year)):
            totalDays += 366
        else:
            totalDays += 365
    # ********** Dias acumulados del año actual al día de hoy **********
    totalDays += calculateElapsedDays(currentDay, currentMonth, currentYear)

    # ** Si el año de nacimiento es el igual al año actual, se calcula la diferencia entre los días acumulados al día actual y los días acumulados a la fecha de nacimiento.
    if(birthYear < currentYear):
        elapsedBirthDays = 365 - calculateElapsedDays(birthDay, birthMonth, birthYear)
        if((birthMonth < 1 or (birthMonth == 1 and birthDay <= 28)) and isLeapYear(birthYear)):
            elapsedBirthDays += 1
        totalDays += elapsedBirthDays
    
    print(f'\nFecha ingresada: {birthDay} {monthCalendar[birthMonth-1]} {birthYear}')
    print(f'Ha vivido {totalDays} día(s).\n')
daysLived()


