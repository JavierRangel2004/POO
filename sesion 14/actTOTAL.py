import os
'''
Instrucciones:
Su mision es crear la clase Alumno, la cual esta definida de la siguiente manera
    Atributos:
        nombre -> String ---------- Obtener su valor como argumento del constructor de la clase
        matricula -> String ---------- Obtener su valor como argumento del constructor de la clase
        materias -> diccionario vacio ---------- Preinicializado dentro del constructor (No toma su valor con el argumento del constructor)
        costo_credito = 2500 ----------Preinicializado dentro del constructor (No toma su valor con el argumento del constructor)

        NOTA: Al crear un objeto, debe imprmirse la frase "Alumn@ {nombre del alumno} ha sido creado con la matricula {matricula del alumno}"
    
    Metodos:
        inscribir_materia
            Argumentos: Recibe un diccionario con los datos corresponientes a cada materia (los diccionarios de estas materias se encuentran mas abajo 
                        en este mismo documento)
            Funcionamiento: El formato del diccionario puede verse en las 3 materias incluidas en este archivo
                            Al inscribri una materia, se debe agregar la informacion correspondiente al diccionario que
                            originalmente estaba vacio dentro de la clase
                            {
                            'nombre de la materia 1': 'datos de la materia 1',
                            'nombre de la materia 2': 'datos de la materia 2',
                            etc
                            }
        
        
        desinscribir_materia
            Argumentos: Nombre de la materia a desinscribir
            Funcionamiento: Borrar el key correspondiente a la materia por desinscribrir
                            (busquen en internet como funciona "del" para diccionarios)
                            Usen un bloque try except para evitar que el programa crashee al intentar
                            desinscribir una materia no existente en el diccionario
        
        
        calcular_colegiatura
            Argumentos: Nada
            Funcionamiento: Calcula el costo total de la colegiatura sumando los creditos de las materias
                            inscritas y multiplicando el resultado por el costo del credito.
                            La suma de creditos inscritos debe hacerse con ciclos for
        
        
        aplicar_beca
            Argumentos: Porcentaje (en flotante. ejemplo: 0.30 es una beca del 30%)
            Funcionamiento: Actualiza el costo por credito de la clase haciendo el descuento correspondiente
        
        
        calificar_materia    
            Argumentos: Nombre de la materia a calificar y calificacion
            Funcionamiento: Asigna la calificacion a la materia correspondiente
                            Y cambia la bandera "Materia Cursada" a True
        
        
        calcular_promedio
            Argumentos: Nada
            Funcionamiento: Usando ciclos for, calcula y devuelve el promedio del alumno
                            El programa debe generar una excepcion (el programa debe crashear)
                            si se intenta sacar el promedio de una materia que aun no ha sido cursada

'''
#Estas son las materias a inscribir
programacion = {
        'nombre':'POO',
        'datos':{
                'Salon':'A',
                'Dias':'Lunes, Martes, Jueves',
                'Creditos':5,
                'Calificacion':0,
                'Materia Cursada':False
           }
           }

animacion = {
        'nombre':'Animacion y jueguitos',
        'datos':{
                'Salon':'B',
                'Dias':' Martes, Jueves',
                'Creditos':'6',
                'Calificacion':0,
                'Materia Cursada':False
           }
           }

algebra = {
        'nombre':'Algebra',
        'datos':{
                'Salon':'D',
                'Dias':'Jueves',
                'Creditos':'4',
                'Calificacion':0,
                'Materia Cursada':False
           }
           }
def clear():
    os.system('cls')

class Alumno():
    def __init__(self,nombre,matricula):
        self.nombre=nombre
        self.matricula=matricula
        self.materias={}
        self.costo_credito=2500
        print(f"Alumn@ {self.nombre} ha sido creado con la matricula {matricula}")
    def inscribir(self,**diccionario):
        self.materias[diccionario['nombre']]=diccionario
    def desinscribir(self,materia):
        try:
            del self.materias[materia]
        except:
            print('La materia no esta inscrita')
    def colegiatura(self):
        coleg=0
        for materia in self.materias:
            coleg+=int(self.materias[materia]['datos']['Creditos'])
        return coleg*self.costo_credito
    def beca(self,per):
        self.costo_credito=self.costo_credito*(1-per)
    def cali_materia(self,materia,cali):
        self.materias[materia]['datos']['Calificacion']=cali
        self.materias[materia]['datos']['Materia Cursada']=True
    def prom(self):
        sum=0
        materias=0
        for materia in self.materias:
            materias+=1
            sum+=self.materias[materia]['datos']['Calificacion']
        return sum/materias


clear()
Alumno1=Alumno("Juan",256158)
Alumno1.inscribir(**algebra)
Alumno1.inscribir(**programacion)
print(Alumno1.materias)
print(f"Colegiatura = {Alumno1.colegiatura()}")
Alumno1.beca(.1)
print(f"Colegiatura = {Alumno1.colegiatura()}")
Alumno1.desinscribir("Algebra")
Alumno1.cali_materia("POO",10)
print(Alumno1.prom())