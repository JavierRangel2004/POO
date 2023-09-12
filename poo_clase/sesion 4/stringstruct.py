frase="Shrek es vida, Shrek es amor"
print(frase)
#imprime el caracter en ese espacio
print(frase[0])
#al estar negativo va de derecha a izquierda
print(frase[-1])
#se concatena del primer al quinto
print("Hola "+frase[:5])
frase=frase.lower().replace("shrek","papoi").upper()
print(frase)
#se concatena pero de izq a derecha
print("El "+frase[-4:].lower()+" apesta")