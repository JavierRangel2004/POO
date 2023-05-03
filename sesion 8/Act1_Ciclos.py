#1 De la siguiente lista, imprima el resultado de elevar cada elemento al cuadrado:
print("Ejercicio 1")
mi_lista = [1,3,9,7,11]
j=0
for i in mi_lista:
    print(f"{mi_lista[j]} al cuadrado = {i**2}")
    j+=1

#2 De la siguiente lista, imprima el resultado de elevar cada elemento al cuadrado:
print("\nEjercicio 2")
mi_lista_2 = [1,'3',9,'7','11']
j=0
for i in mi_lista_2:
    print(f"{mi_lista_2[j]} al cuadrado = {int(i)**2}")
    j+=1

#3 De la siguiente lista, imprima el resultado de elevar cada elemento al cuadrado. Solo castear 
#tipo de datos cuando se requiera. No castear todo el tiempo
print("\nEjercicio 3")
mi_lista_2 = [1,'3',9,'7','11']
j=0
for i in mi_lista_2:
    if(type(i)==str):
      print(f"{mi_lista_2[j]} al cuadrado = {int(i)**2}")
    else:
        print(f"{mi_lista[j]} al cuadrado = {i**2}")
    j+=1

#4 Recorrer con un for la siguiente lista de nombres, imprimir "Hola nombre_en_la lista" por cada nombre
print("\nEjercicio 4")
nombres =['Cheems','Cholondrina','Medio Metro']
for nom in nombres:
    print(f"Hola {nom}")

#5 Pedir al usuario un valor inicial, un valor final y el tipo de cambio
#Realizar un conversor de divisas donde se imprima el resultado de multiplicar desde al valor
#inicial al valor final por el tipo de cambio.
#Ejemplo, si el valor inicial es 1 y el final es 3, con un tipo de cambio de 10, debera mostrarse:
#1 dolar son 10 pesos
#2 dolar son 20 pesos
#3 dolares son 30 pesos
print("\nEjercicio 5")
inicial=int(input("Ingresa un valor inicial: "))
final=int(input("Ingresa un valor final: "))
camb=int(input("Ingresa un tipo de cambio: "))
for i in range(inicial,final+1):
    print(f"{i} dolares = {i*camb} pesos")

#6 Pedir al usuario un valor inicial y un valor final, devolver una lista con un rango de valores
#entre esos numeros que contenga el valor al cubo de los mismos, por ejemplo, si 1 es inicial y 
#3 es final, la lista resultante debe ser [1,8,27]
print("\nEjercicio 6")
inicial=int(input("Ingresa un valor inicial: "))
final=int(input("Ingresa un valor final: "))
#list comprenhension
listc=[i**3 for i in range(inicial,final+1)]
print(listc)