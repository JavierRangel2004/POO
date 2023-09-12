edad=input("Ingresa tu edad: ")
print(type(edad))
#El casteo es en la linea por lo que no se guarda
print(f"En 20 años tendrias {int(edad)+20}")
print(type(edad))
#El input lo transforma a mayusculas
nombre=input("Ingresa tu nombre: ").upper()
print(nombre)
#print(length(nombre))
nom="Hola como estas?"
print(nom)
#el resultado de in o not in devuelve un bool dependiendo si esta o no en el str
print("como"in nom)
#cuenta la cantidad de veces que aparece el str dado en otra variable str
print(f"como sale {nom.count('como')} veces en hola como estas ")