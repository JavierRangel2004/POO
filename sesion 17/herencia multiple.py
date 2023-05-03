class Agenda():
  def __init__(self):
    self.lista_contacto={}
    print("Este telefono tiene agenda")
  def agregar(self,nombre,num):
    self.lista_contacto[nombre]=num

class camera():
  def __init__(self,megap):
    self.megapixeles=megap
    print(f"Esta camara toma fotos con {megap} megapixeles de resolucion")
  def foto(self):
    print(f"Tomando foto con {self.megapixeles} de resolucion")

class reproductor():
  def __init__(self):
    self.lista_c=[]
  def agregar_c(self,cancion):
    self.lista_c.append(cancion)

'''
agenda1=Agenda()
agenda1.agregar("jose",52615)
print(agenda1.lista_contacto)
camara1=camera(42)
camara1.foto()
repro1=reproductor()
repro1.agregar_c("Puto")
print(repro1.lista_c)
'''

class cel(Agenda,camera,reproductor):
  def __init__(self,megap):
    Agenda.__init__(self)
    camera.__init__(self,megap)
    reproductor.__init__(self)

cel1=cel(80)
cel1.foto()
cel1.agregar("Juanito",2561584)
cel1.agregar_c("Nothing else matters")
print(cel1.lista_contacto)
print(cel1.lista_c)

class Auto():
  def __init__(self):
    self.__velocidad=0
    print(self.__velocidad)
  def subirvel(self,aumento):
    self.__velocidad+=aumento
    print(f"Velocidad= {self.__velocidad} km/h")
  def bajarvel(self,decremento):
    self.__velocidad-=decremento
    print(f"Velocidad= {self.__velocidad} km/h")
auto1=Auto()
auto1.bajarvel(100)
auto1.subirvel(264)
auto1.bajarvel(104)