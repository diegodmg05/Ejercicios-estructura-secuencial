#Calcular el perímetro y área de un rectángulo dada su base y su altura.
import math
#Entrada de datos:
base = float(input("Dime base: "))
altura = float(input("Dime altura: "))
perimetro = 2*base + 2*altura
area = base*altura
#Salida de datos
print("Base: ",base)
print("Altura: ",altura)
print("Perimetro: ",round(perimetro,2))
print("Area: ", round(area, 2))