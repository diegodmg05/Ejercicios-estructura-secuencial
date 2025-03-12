# Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

#Librerias a importar
import math
#Entrada de datos
cateto1 = float(input("Dime cateto 1: "))
cateto2 = float(input("Dime cateto 2: "))
hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2) # Otra forma:  math.sqrt(pow(cateto1, 2)+ pow(cateto2, 2))
#Salida de datos
print("cateto1: ", cateto1, " cateto2: ", cateto2, " Hipotenusa: ", round(hipotenusa,2)) 