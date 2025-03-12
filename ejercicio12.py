"""
Ejercicio 12
Pide al usuario dos pares de números x1,y1 y x2,y2, que representen dos puntos en el plano. Calcula y muestra la distancia entre ellos.
"""
import math

#Introducir datos
x1 = int(input("Dime valor para x1: "))
y1 = int(input("Dime valor para y1: "))
x2 = int(input("Dime valor para x2: "))
y2 = int(input("Dime valor para y2: "))
#Calcular la diferencia de x2, x1
x = x2 - x1
#Calcula la direrencia de y2, y1
y = y2 - y1
#Calcular la diferencia entre x e y
total = pow(x, 2) + pow(y, 2)
#Imprimir resultado
print("Distancia final: %.2f" % math.sqrt(total))
