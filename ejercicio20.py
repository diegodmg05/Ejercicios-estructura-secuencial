"""
Ejercicio 20
Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).
"""
num_2euros = int(input("Dime numero de monedas de dos euros: "))
num_1euro = int(input("Dime numero de monedas de un euro: "))
num_50cent = int(input("Dime numero de monedas de 50 céntimos: "))
num_20cent = int(input("Dime numero de monedas de 20 céntimos: "))
num_10cent = int(input("Dime numero de monedas de 10 céntimos: "))
#Pasamos todo a centimos
total = ((num_2euros*200) + (num_1euro*100)+ (num_50cent*50) + (num_20cent*20) + (num_10cent*10)) //100
centimos = ((num_2euros*200) + (num_1euro*100)+ (num_50cent*50) + (num_20cent*20) + (num_10cent*10)) %100
#Imprimos los resultados
print("Euros: ", total, "centimos: ", centimos)