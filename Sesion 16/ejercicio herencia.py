import os
def clear():
    os.system('cls')

class Vehiculo():
    def __init__(self, numero_ruedas, velocidad):
        self.numero_ruedas = numero_ruedas
        self.velocidad = velocidad
        print(f"Vehiculo creado!")

    def desplazarse(self):
        print(f"Vehiculo desplazandose!")

'''
A partir de la clase padre, crear las siguientes clases hijas
Avion
    Metodos
        sonar_claxon
            Argumentos: Nada
            Comportamiento: Imprimir "My sonic claxon goes NOOT NOOT"
Microbus
    Metodos
        sonar_claxon
            Argumentos: Nada
            Comportamiento: Imprimir "Grito de tarzan bien macizo"
Automovil
    Metodos
        sonar_claxon
            Argumentos: Nada
            Comportamiento: Imprimir "MIC MIC"
Bicicleta
    Metodos
        sonar_claxon
            Argumentos: Nada
            Comportamiento: Imprimir "Sonido de corneta"

Usando polimorfismo, crear un metodo "desplazarse" con los siguientes comportamientos para las clases hijas:
    Clase Avion: Imprimir "Volando sin llantas"
    Clase Microbus: Imprimir "Rodando en 4 llantas, o a veces 3"
    Clase Automovil: Imprimir "Rodando en 4 llantas"
    Clase Bicicleta: Imprimir "Rodando en 2 llantas"
'''
class Avion(Vehiculo):
    def __init__(self, numero_ruedas, velocidad):
        super().__init__(numero_ruedas, velocidad)
    def claxon(self):
        print("Grito de tarzan bien macizo")
    def desplazarse(self):
        print("Volando sin llantas")

class Auto(Vehiculo):
    def __init__(self, numero_ruedas, velocidad):
        super().__init__(numero_ruedas, velocidad)
    def claxon(self):
        print("MIC MIC")
    def desplazarse(self):
        print("Rodando en 4 llantas, o a veces 3")

class Bici(Vehiculo):
    def __init__(self, numero_ruedas, velocidad):
        super().__init__(numero_ruedas, velocidad)
    def claxon(self):
        print("Sonido de corneta")
    def desplazarse(self):
        print("Rodando en 2 llantas")
clear()
avion1=Avion(6,269)
coche1=Auto(4,258)
bici1=Bici(2,35)
avion1.desplazarse()
coche1.claxon()
bici1.desplazarse()