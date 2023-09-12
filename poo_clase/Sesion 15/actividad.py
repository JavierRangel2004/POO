'''
Instrucciones:
Su mision es crear la clase Alumno, la cual esta definida de la siguiente manera
    Atributos:
        nombre -> String ---------- Obtener su valor como argumento del constructor de la clase
        matricula -> String ---------- Obtener su valor como argumento del constructor de la clase
        materias -> lista vacia ---------- Preinicializado dentro del constructor (No toma su valor con el argumento del constructor)
        costo_credito = 2500 ----------Preinicializado dentro del constructor (No toma su valor con el argumento del constructor)

        NOTA: Al crear un objeto, debe imprmirse la frase "Alumn@ {nombre del alumno} ha sido creado con la matricula {matricula del alumno}"
    
    Metodos:
        inscribir_materia
            Argumentos: Recibe el nombre de una materia, la cual se añade a la lsita de materias del alumno
            Funcionamiento: Al inscribir la materia, debe imprimirse la frase "la materia {materia} ha sido inscrita correctamente"
        
        
        calcular_colegiatura
            Argumentos: Nada
            Funcionamiento: Calcula el costo total de la colegiatura multiplicando el costo del credito X el numero de materias X 5
              (asumamos que cada materia tiene una carga de 5 creditos)
        
        
        aplicar_beca
            Argumentos: Porcentaje (en flotante. ejemplo: 0.30 es una beca del 30%)
            Funcionamiento: Actualiza el costo por credito de la clase haciendo el descuento correspondiente
        
'''
class Alumno:
    def __init__(self,nombre,matricula):
        self.nombre=nombre
        self.matricula=matricula
        self.materias=[]
        self.costocredito=2500
        print(f"Alumn@ {self.nombre} ha sido creado con la matricula {matricula}")
    def inscribir(self,materia):
        self.materias.append(materia)
        print(f"La materia {materia} ha sido inscrita correctamente.")
    def colegiatura(self):
        print(f"Colegiatura = {(len(self.materias)*5*self.costocredito)}")
    def beca(self,porcentaje):
        self.costocredito=(self.costocredito*(1-porcentaje))

alumno1=Alumno("Juan","0256158")
alumno1.inscribir("Mate")
alumno1.inscribir("Poo")
alumno1.colegiatura()
alumno1.beca(.5)
alumno1.colegiatura()