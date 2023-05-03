import funciones
#celsius a farenheit = (celsisus * 9/5) + 32

#funcion que reciba tantos nombres como sea posible
#1er nombre, nombre de usuario
#2do nombre, nombre del bff
#El resto, amigos
#imprimir nombre de usuario, nombre del bff y amigos



# nombres=[]
# tope=int(input("Ingresa cuantos nombres quieres ingresar: "))
# for i in range(tope):
#     nombres.append(input(f"Ingresa nombre {i+1}: "))

grados=int(input("Ingresa los grados celsius: "))
print(f"{grados}°C = {funciones.farenheit(grados)}°F")

nombres=[]
des=1
while des==1:
    desnom=input("Ingresa nombre (o 0 para salir) : ")
    if desnom!="0":
        nombres.append(desnom)
    else:
        des=0
funciones.amigos(*nombres)