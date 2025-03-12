"""
Ejercicio 19
Escribir un algoritmo para calcular la nota final de un estudiante, considerando que: por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. Imprime el resultado obtenido por el estudiante.
"""
#Introducir valores
correctas = int(input("Dime número de respuestas correctas: "))
incorrectas = int(input("Dime número de respuestas incorrectas: "))

#Total puntos
total = (correctas*5) - (incorrectas * 1)
#Imprimir puntuacion final:
print("Puntuacion final: %.2f" % total)