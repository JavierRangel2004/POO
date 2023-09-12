import os
def clear():
    os.system('cls')

class Persona():
    def __init__(self,nombre,matricula,fecha_alta):
        self.nombre=nombre
        self.matricula=matricula
        self.fecha=fecha_alta
    def saludar(self):
        print(f"La persona {self.nombre} con la matricula {self.matricula} se dio de alta en la fecha: {self.fecha}")

class Estudiante(Persona):
    def __init__(self, nombre, matricula, fecha_alta,promedio):
        super().__init__(nombre, matricula, fecha_alta)
        self.promedio=promedio
    def saludar(self):
        print(f"Hola soy {self.nombre}, mi matricula es {self.matricula} y me dieron de alta en la fecha: {self.fecha}")

class Profesor(Persona):
    def __init__(self, nombre, matricula, fecha_alta,sueldo):
        super().__init__(nombre, matricula, fecha_alta)
        self.sueldo=sueldo

import datetime
clear()
persona1=Persona("Juan","0256158",datetime.datetime.now())
persona1.saludar()
estudiante1=Estudiante("Carlos","09856",datetime.datetime.now(),9.86)
estudiante1.saludar()
profesor1=Profesor("Ivan","159357",datetime.datetime.now(),25000)
profesor1.saludar()