"""
Ejercicio 16
Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro.
"""
import math
#Introducir valores 
distancia = float(input("Dime distancia entre los dos vehículos: "))
velocidad_1 = float(input("Dime velocidad 1: "))
velocidad_2 = float(input("Dime velocidad 2: "))
tiempo  = distancia / (velocidad_1- velocidad_2)
tiempo = tiempo * 60
print("Va ha tardar  ", abs(tiempo), " minutos")
