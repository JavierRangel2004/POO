#dry dont repeat yourself
import os

#funciones
def hola(nombre):
    print(f"Hola {nombre}")

def clear():
    input("Presiona enter para continuar.")
    os.system("cls")

def saludo(nom,edad):
    print(f"Hola {nom}, tienes {edad} años.")

def suma(n1,n2):
    return n1+n2

clear()
nom=input("Ingresa tu nombre: ")
edad=input("Ingresa tu edad: ")
saludo(nom,edad)
clear()
n1=int(input("Ingresa numero 1: "))
n2=int(input("Ingresa numero 2: "))
print(f"Suma de los dos numeros = {suma(n1,n2)}")
clear()
#input en un print, primero pregunta nombre y luego imprime
print(f"Hola {input('Nombre: ')}")

