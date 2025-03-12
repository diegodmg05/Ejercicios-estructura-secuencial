"""
Ejercicio 9
Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.
"""
import math
#Introduccion datos
precio_base = float(input("Dime precio base de la compra: "))
#Calcula el precio total aplicando el descuento
precio_total = precio_base - (precio_base * 0.15)
#Resultado final
print("El precio final es: ", round(precio_total, 2))
