"""
Ejercicio 11
Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).
"""
import math
#Introducir datos
#Se considera que puede sen float
num_1 = float(input("Dime numero 1: "))
num_2 = float(input("Dime numero 2: "))
#Calcular distancia 
distancia = num_1 - num_2
#Resultado final
print("Distancia total: %.2f" % abs(distancia))