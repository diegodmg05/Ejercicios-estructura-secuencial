#Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es:
#C = (F-32)*5/9
import math
#Entrada de datos
temp = float(input("Dime una cantidad de grados fahrenheit: "))
f = (temp-32)*5/9
#Salida de datos:
print(round(f, 2), "ºC")