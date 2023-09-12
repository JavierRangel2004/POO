#Pida al usuario su edad. Si tiene 18 anios o mas, imprimir "Eres mayor de edad"
#En caso contrario, imprimir "eres menor de edad"
edad=int(input("Ingresa tu edad= "))
if(edad>=18):
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
#En el mismo programa, indique si la edad del usuario es un numero par o un numero impar
if(edad%2==0):
    print("Es par.")
else:
    print("Es impar.")
#Si la edad esta entre 30 y 40, imprimir "Ya sientese, senior(a)"
if(edad>30 & edad<40):
    print("Ya sientese señor(a)")
