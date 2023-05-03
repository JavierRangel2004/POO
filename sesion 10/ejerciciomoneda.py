def listaconversion(nombre,min,max,cambio):
    print(f"Bienvenido {nombre} a la lista de conversion de dolares a pesos")
    for i in range(min,max+1):
        print(f"{nombre} {i} = {i*cambio}")
    return cant*cambio
cant=int(input("Ingresa la cantidad de dolares: "))
cambio=float(input("Ingresa el tipo de cambio: "))