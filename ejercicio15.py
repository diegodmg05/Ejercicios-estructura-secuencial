"""
Ejercicio 15
Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.
"""
#Introducir valores
a = int(input("Dime valor para A: "))
b = int(input("Dime valor para B: "))
#Intercambiar valores
#Guardar el valor anterior de a
aux = a
a = b
b = aux
print("A: ", a)
print("B: ", b)