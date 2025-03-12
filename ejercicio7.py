#Ejercicio 7
#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
#Por ejemplo: 1000 minutos son 16 horas y 40 minutos.
num = int(input("Dime una cantidad de minutos: "))
horas = num // 60
minutos = num % 60

print("Es equivalente a ",horas," horas y ", minutos, "minutos")