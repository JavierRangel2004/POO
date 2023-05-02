import requests
import os
import pandas as pd
import datetime
import json
def clear():
    input("Presiona enter para continuar...")
    os.system('clear')
#Has un programa que pueda hacer cotizaciones para un cliente, el programa debe de pedir el nombre del cliente, DATOS el programa debe de guardar la cotización en un archivo de texto con el nombre del cliente y la fecha de la cotización.
class Cliente():
    def __init__(self,nombre):
        self.cotizacion={}
        self.servicios=1
        self.guardado=False
        self.cotizacion["Fecha"]=str(datetime.datetime.now())
        self.cotizacion["Nombre del cliente"]=nombre
        print(f"Cotizacion para el cliente {self.cotizacion['Nombre del cliente']}")
    def Total_a_pagar(self):
        total=0
        for i in self.cotizacion:
            if i.startswith("Precio"):
                total+=self.cotizacion[i]
        return total
    def agregar(self):
        #while True:
            #print("1.- Agregar servicio")
            #print("2.- Salir")
            #op=int(input("Elige una opción: "))
            #if op==1:
                #clear()
                #agrega valores del servicio tomando en cuenta que se pueden agregar varios servicios (evita que se sobreescriban los valores del diccionario)
                self.cotizacion[f"Nombre del servicio {self.servicios}"]=input("Ingresa el nombre del servicio: ")
                self.cotizacion[f"Descripcion del servicio {self.servicios}"]=input("Ingresa la descripción del servicio: ")
                self.cotizacion[f"Precio del servicio {self.servicios}"]=int(input("Ingresa el precio del servicio: "))
                self.cotizacion[f"Total a pagar"]=self.Total_a_pagar()
                if self.servicios>0:
                    temp_value = self.Total_a_pagar()
                    self.cotizacion.pop("Total a pagar")
                    self.cotizacion["Total a pagar"] = temp_value
                self.servicios+=1
                clear()

            #elif op==2:
                #break
            #else:
                #print("Opción no válida")
    def mostrar(self):
        print(f"Cotización para el cliente {self.cotizacion['Nombre del cliente']}")
        #impimir los valores: nombre del servicio,precio del servicio, total a pagar
        for i in self.cotizacion:
            if not i.startswith("Fecha") and not i.startswith("Nombre del cliente") and not i.startswith("Descripcion"):
                print(f"{i}: {self.cotizacion[i]}")
    def guardar(self):
        self.mostrar()
        print("Los datos de la cotizacion son correctos? (s/n)")
        op=input()
        clear()
        if op=="s":
            with open(f"{self.cotizacion['Nombre del cliente']}.txt","a") as archivo:
                if self.guardado==False:
                    archivo.write(f"Cotización para el cliente {self.cotizacion['Nombre del cliente']} hecha en la fecha {str(datetime.datetime.now())}\n")
                for i,value in enumerate(self.cotizacion.values(),1):
                    if i<len(list(self.cotizacion.values())):
                        archivo.write(f"{str(value)},")
                    else:
                        archivo.write(f"{str(value)}")


            print("Se guardaron los datos de la cotización")
            clear()
        else:
            print("Se boraran los datos de la cotización")
            self.cotizacion={}
            clear()
def menu():
        print("1.- Agregar cliente")
        print("2.- Mostrar clientes")
        print("3.- Mostrar servicios")
        print("4.- Salir")
        op=int(input("Elige una opción: "))
        clear()
        return op
def nvocliente():
    nombre=input("Ingresa el nombre del cliente: ")
    clear()
    cliente=Cliente(nombre)
    cliente.agregar()
    cliente.guardar()
    return cliente
def main():
    clientes=[]
    while True:
        op=menu()
        if op==1:
            clientes.append(nvocliente())
        elif op==2:
            for i in clientes:
                print(i.cotizacion["Nombre del cliente"])
            clear()
        elif op==3:
            for i in clientes:
                i.mostrar()
            clear()
        elif op==4:
            break
        else:
            print("Opción no válida")
            clear()
main()
#Buscar los archivos de cotizacion y hacer un archivo .csv con los datos de las cotizaciones
def archivocompleto():
    with open("cotizaciones.csv","a") as archivo:
        if os.stat("cotizaciones.csv").st_size==0:
            archivo.write("Fecha,Cliente,Nombre del servicio,Descripcion,Precio\n")
def xd():
    archivos = os.listdir()
    for i in archivos:
        if i.endswith(".txt"):
            with open(i, "r") as archivo:
                datos = archivo.readlines()[1:]
                datos = datos[0].split(",")
                with open("cotizaciones.csv", "a") as archivo2:
                    for i in range(len(datos)-1):
                        archivo2.write(f"{datos[i]},")
                        if i == len(datos):
                            archivo2.write(f"{datos[i]}")

                    archivo2.write("\n")
archivocompleto()
xd()