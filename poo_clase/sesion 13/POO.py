class MedioMetroRobot():
    def __init__(self,nombre_usuario,procedencia):
        self.nombre=nombre_usuario
        self.procede=procedencia
        print(f'Ha nacido un robot Medio Metro procedente de {self.procede} y se llama {self.nombre}')
    altura=0.5
    material="aluminio"
    altura=0.5
    material="aluminio"
    def Saludar(self):
        print(f"Te quiero {self.nombre}")

robot1=MedioMetroRobot('Carlos','México')
robot1.Saludar()
print(isinstance(robot1,MedioMetroRobot))
print(type(robot1))
robot2=MedioMetroRobot('Juan','España') 