import os
def limpiar():
    os.system("cls")
numero1=3
numero2=0
#print(numero2/numero1)
nombres=['A','B']
#Mensaje de error, ayuda con las APIs
limpiar()
try:
    print(nombres[2])
except IndexError:
    print("Hay menos elementos en la lista del que quieres imprimir")
try:
    print(numero2/numero2)
except ZeroDivisionError:
    print("Division entre 0 = No papito")

#Has una funcion que limpie la consola