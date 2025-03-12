"""
Ejercicio 18
Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.
"""
#Introducir valores
nombre = str(input("Dime nombre: "))
primer_apellido = str(input("Dime primer apellido: "))
segundo_apellido = str(input("Dime segundo apellido: "))
#Cogemos la primea letra de cada variable
iniciales = nombre[0] + primer_apellido[0] + segundo_apellido[0]
#Imprimir iniciales
print("Iniciales: ", iniciales.upper())