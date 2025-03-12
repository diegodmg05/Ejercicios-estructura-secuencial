#Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.
import math
#Entrada de datos
num1 = float(input("Dime un número: "))
num2 = float(input("Dime otro número: "))
suma = num1 + num2
resta = num1 - num2
multiplicación = num1 * num2
division = num1 / num2
#Salida de datos
print("Suma: ", round(suma, 2))
print("Resta: ", round(resta, 2))
print("Multiplicación: ", round(multiplicación, 2))
print("División: ", round(division, 2))