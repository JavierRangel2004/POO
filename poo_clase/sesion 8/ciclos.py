numero=0
while numero<6:
    print(numero)
    numero+=1

numeros= range(1,11,2)#Se detiene uno antes, del uno al once y va de 2 en 2
print(list(numeros))

for i in range(1,11):
    print(f"{i} hola")

#desempaquetando estructuras
amigos=["Esteban","Daniel","Vitela","Santiago"]
for amigo in amigos:
    print(f"Chinga tu madre {amigo}")