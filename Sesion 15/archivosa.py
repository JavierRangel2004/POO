import os

def clear():
    input("Presiona enter para continuar...")
    os.system('cls')
class Persona():
    def __init__(self,nombre,edad):
        self.nombre =nombre
        self.edad=edad
        print(f"Se creo la persona {nombre} con {edad} años de edad")
    def respirar(self):
        print(f"{self.nombre} respiró...")

class alumno(Persona):
    def __init__(self, nombre, edad,promedio,carrera):
        super().__init__(nombre, edad)
        self.prom=promedio
        self.carrera=carrera
        with open("alumnos.txt","a") as archivo:
            archivo.write(f"Se creo un alumno {nombre} con {edad} años de edad y promedio {promedio} en la carrera {carrera}\n")
    def setprom(self,cali):
        self.prom=cali

clear()
alumno1=alumno("Juan",20,9.5,"Ingenieria en computacion")
alumno1.setprom(10)
alumno1.respirar()
alumno2=alumno("Pedro",21,6.4,"Ingenieria Mecanica")
alumno2.respirar()
