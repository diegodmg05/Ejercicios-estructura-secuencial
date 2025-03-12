#Calcular la media de tres números pedidos por teclado.
import math
#Entrada de datos
num1 = float(input("Dime num1: "))
num2 = float(input("Dime num2: "))
num3 = float(input("Dime num3: "))
media = (num1+num2+num3) / 3
#Salida de datos
print("Media: ", round(media, 2))