"""
Ejercicio 10
Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
•	55% del promedio de sus tres calificaciones parciales.
•	30% de la calificación del examen final.
•	15% de la calificación de un trabajo final.

"""
import math

#Promedio de las tres calificaciones
nota_1 = float(input("Dime nota 1: "))
nota_2 = float(input("Dime nota 2: "))
nota_3 = float(input("Dime nota 3: "))
#Calculamos la nota media
media = (nota_1+nota_2+nota_3) / 3
#Calculamos el promedio
promedio = media * 0.55
#Calculamos la nota del examen final
ex_final = float(input("Dime nota del examen final: "))
nota_final = ex_final * 0.3
#Calculamos la nota del trabajo final
trabajo_final = float(input("Dime nota del trabajo final: "))
nota_trabajo = trabajo_final* 0.3
#Calculamos la calificacion final de la materia
nota_materia = promedio + nota_final + nota_trabajo
#Imprimir resultado
print("Calificacion final de la materia es ", round(nota_materia, 2))