def farenheit(celsius):
    return (celsius * 9/5) + 32

def amigos(*nombres):
    print(f"Hola {nombres[0]}")
    print(f"Nombre de tu mejor amigo: {nombres[1]}")
    print("Amigos:")
    for i in range(2,len(nombres)):
        print(nombres[i])
        
def info_user (**diccionario):
    for llave,valor in diccionario.items():
        print(f"{llave} = {valor}")