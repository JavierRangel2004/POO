'''
Crear la clase Medio Metro Robot
La misma estara compuestas de los siguientes metodos y atributos
Atributos:
    -anio de fabricacion  ->int
    -lote  ->int 
    -material  ->string
    -altura  ->float
    -coeficiente intelectual  ->float
    -pasos  -> list

Al ser instanciado un objeto de esta clase, debe imprimirse "Hola. Me fabricaron en {anio de fabricacion} y soy 
parte del lote {lote}

Metodos:
    -saludar
        Debe imprimir "Hola, seamos cumbiamigos"
    -decir coeficiente
        Debe imprimir "Mi coeficiente es de {coeficiente}"
    -listar pasos
        Debe imprimir los pasos que conoce el medio metro (usar ciclos for pa imprimirlos)
    - aprender pasos
        Debe recibir como argumento el nombre de un paso, que sera agregado a la lista de pasos 
        que se sabe

'''
class MedioMetroRobot():
    def __init__(self,anio,lote,coeficiente):
        self.anio=anio
        self.lote=lote
        self.coeficiente=coeficiente
        self.pasos=["chaquetita","cabeceo","corazon"]
        print(f'Hola. Me fabricaron en {self.anio} y soy parte del lote {self.lote}')
    material="aluminio"
    altura=0.5
    def saludar(self):
        print("Hola, seamos cumbiamigos")
    def decir_coeficiente(self):
        print(f'Mi coeficiente es de {self.coeficiente}')
    def listar_pasos(self):
        for paso in self.pasos:
            print(paso)
    def aprender_pasos(self,nuevo_paso):
        self.pasos.append(nuevo_paso)
        print(f'He aprendido el paso {nuevo_paso}')

robot1=MedioMetroRobot(2020,1,0.5)
robot1.saludar()
robot1.decir_coeficiente()
robot1.listar_pasos()
robot1.aprender_pasos('cumbia')