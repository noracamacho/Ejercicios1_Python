# Reciba la velocidad y la distancia que tiene que recorrer un carro y entrega cuánto tiempo le tomaría recorrer esa distancia.
import math
def calculateTime(distance, speed):
    speed = speed / 3600
    time = math.floor(distance / speed)
    hrs = math.floor(time / 3600)
    min = math.floor((time % 3600) / 60)
    sec = (time % 60) % 60
    return {"hrs" : hrs, "min" : min, "sec" : sec}

distance = int(input("\nIngrese la distancia a recorrer (km): "))
speed = int(input("Ingrese la velocidad del vehiculo (km/hr): "))
time = calculateTime(distance, speed)
print(f'Te tomará {time['hrs']} hrs, {time['min']} min, {time['sec']} seg llegar a tu destino.\n')