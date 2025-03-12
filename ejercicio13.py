"""
Ejercicio 13
Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica. Python3 no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿Cómo se puede calcular?
"""
import math

#Introducir datos
num = int(input("Dime número: "))
#Calcular raices
raiz_cuadrada = math.sqrt(num)
raiz_cubica = num ** (1/3)
#Imprimir valores
print("Raiz cuadrada: %.2f" % raiz_cuadrada)
print("Raiz cuadrada: %.2f" % raiz_cubica)
