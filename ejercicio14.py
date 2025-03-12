"""
Ejercicio 14
Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. Ejemplo, si se introduce 23 que muestre 32.
"""
#Introducir numero
num = int(input("Dime numero: "))
#numero invertido
print("Numero invertido: ",num %10, num // 10)