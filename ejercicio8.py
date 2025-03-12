"""Ejercicio 8
Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.
"""
import math

sueldo_base = float(input("Dime sueldo base: "))
venta_1 = float(input("Dime venta 1: "))
venta_2 = float(input("Dime venta 2: "))
venta_3 = float(input("Dime venta 3: "))
comision = (venta_1 * 0.1) + (venta_2*0.1) + (venta_3 + 0.1)
total = sueldo_base + comision
print("EL total del sueldo del mes es : ",total)
