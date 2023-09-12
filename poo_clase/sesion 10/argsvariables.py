def sumavariable(*numeros):
    resultado=0
    for numero in numeros:
        resultado+=numero
    return resultado

print(sumavariable(1,2,3,4,5,6,7,8,9,10))

list_num=[1,2,3,4,5,6,7,8,9,10]
print(sumavariable(*list_num))

lista=[]
num=int(input("Ingresa cuantos numeros quieres sumar: "))
for i in range(num):
    lista.append(int(input(f"Ingresa numero {i+1}: ")))
print(sumavariable(*lista))

numerossuma=input("Ingresa los numeros a sumar separados por coma: ")
numerossuma=numerossuma.split(",")
#map convierte los elementos de la lista en enteros
numerossuma=list(map(int,numerossuma))
print(sumavariable(*numerossuma))