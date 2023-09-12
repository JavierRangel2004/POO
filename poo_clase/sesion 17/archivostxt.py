import datetime
mascotas=['meyli','sexy','perro','gato','loro']

with open('logeo.txt','w') as file:
    for mascota in mascotas:
        file.write(f"{mascota} se dio de alta a las {datetime.datetime.now()}\n")



class Alumno():
    def __init__(self,matricula,nombre):
        self.__mat=matricula
        self.__nom=nombre 
        self.materias={}
        with open("log_estudiante.txt",'w') as file:
            file.write(f"El alumno {nombre} con matricula {matricula} se creo en la fecha: {str(datetime.datetime.now())}")
    def inscribir_materia(self,materia,creditos):
        self.materias[materia]={'Creditos':creditos}
        print(f"La materia {materia} se inscribio en la fecha: {str(datetime.datetime.now())}")
    def desinscribir_materia(self,materia):
        del self.materias[materia]
        print(f"La materia {materia} se desinscribio en la fecha: {str(datetime.datetime.now())}")

al1=Alumno("0256158","Javier Rangel")
al1.inscribir_materia("Español",8)
al1.inscribir_materia("POO",9)
al1.desinscribir_materia("Español")