'''
1) Imprimir la frase "Efren es alumno del curso de Python"
'''
alumnos = ['Efren','Sara', 'Carlos','Garza']
print(alumnos[0]+" es el alumno del curso de Python.")

'''
2) Crear una lista donde el dato 0 sea el nombre de usuario y el dato 1 sea su edad. 
Los datos deben recolectarse usando "input", la edad debe guardarse como un entero dentro de la lista
Imprimir estructura resultante
'''
info=[input("Ingresa tu nombre: "),int(input("Ingresa tu edad: "))]
print (info)
'''
3) De la lista anterior, cambiar la edad por el doble de su valor. Imprimir estructura resultante
'''
info[1]=2*info[1]
print (f"Doble de la edad: {info}")

'''
4) Indicar cuantos nombres unicos de alumnos existen en la siguiente estructura de datos
'''         
alumnos2 = ['Oscar', 'Daniel',' Amiel', 'Alejandra', 'Danna', 'Daniel', 'Danna','Adrian',' Amiel', 
'Danna', 'Daniel',' Amiel',' Amiel', 'Danna','Oscar','Ivan', 'Diego', 'Daniel']
alumnos2=set(alumnos2)
alumnos2=list(alumnos2)
print(f"Existen {len(alumnos2)} nombres unicos.")
'''
5) Cambiar "Velma" por "The Last of Us" en la siguiente estructura de datos
'''
los_mejores_shows = ('House of the Dragon', 'Rick & Morty', 'Celebrity Deathmatch', 'Velma')
los_mejores_shows=list(los_mejores_shows)
los_mejores_shows[-1]="The Last of Us"
los_mejores_shows=tuple(los_mejores_shows)
print(los_mejores_shows)

'''
6) Imprimir la frase "La alumna Alejandra tiene 9 de promedio
'''
estudiantes = [('Oscar',9),('Alejandra',9),('Ivan',7)]
print(f"La alumna {estudiantes[1][0]} tiene {estudiantes[1][1]} de promedio")

'''
7) Imprimir la frase "El Alumno Oscar esta inscrito en Animacion 101
'''
estudiantes2 = [('Oscar',['Animacion 101','Finanzas']),
('Alejandra',['Matematicas Avanzadas','Hackeo Avanzado']),
('Ivan',['Memelogia','Como entrenar a tu dragon'])]
print(f"El Alumno {estudiantes2[0][0]} esta inscrito en {estudiantes2[0][1][0]}")
'''
8) Cambiar la materia "Memelogia" a "Teoria Sonidera Aplicada". Imprimir estructura resultante
'''
estudiantes2 = [('Oscar',['Animacion 101','Finanzas']),
('Alejandra',['Matematicas Avanzadas','Hackeo Avanzado']),
('Ivan',['Memelogia','Como entrenar a tu dragon'])]
estudiantes2[2][1][0]="Teoria Sonidera Aplicada"
print(estudiantes2)