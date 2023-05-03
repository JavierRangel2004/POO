musica = {
    'The Black Keys':{
        'El Camino':{
            'Lonely Boy':{
                'liked':False,
                'reproducciones':'397810130',
                'duracion_ms':187800,
                'tags':('Rock','Catchy Tunes')
            },
            'Little Black Submarines':{
                'liked':True,
                'reproducciones':'89206240',
                'duracion_ms':246600,
                'tags':('Rock & Roll','Classics','Blues','Ballad',
                        'Rock','Ballad','Blues','Classics','Classics',
                        'Ballad','Rock & Roll','Classics','Blues',
                        'Rock & Roll','Classics','Rock & Roll','Blues')
            },
            'Hell of a Season':{
                'liked':True,
                'reproducciones':10425570,
                'duracion_ms':207000,
                'tags':('Rock')
            }
        }
    },
    'Greta Van Fleet':{
        'From the Fires':{
            'Safari Song':{
                'liked':True,
                'reproducciones':104450524,
                'duracion_ms':'212400',
                'tags':('Rock','Classics')
            },
            'Edge of Darkness':{
                'liked':False,
                'reproducciones':'47756093',
                'duracion_ms':256800,
                'tags':('Rock')
            },
            'Highway Tune':{
                'liked':True,
                'reproducciones':'181238080',
                'duracion_ms':180000,
                'tags':('Hard Rock')
            },
            'Black Smoke Rising':{
                'liked':True,
                'reproducciones':119129373,
                'duracion_ms':251400,
                'tags':('Rock','Classics')
            }
        },
        'The Battle at Gardens Gate':{
            'Heat Above':{
                'liked':True,
                'reproducciones':67071430,
                'duracion_ms':324600,
                'tags':('Rock','Ballad')
            },
            'Age of Machine':{
                'liked':False,
                'reproducciones':'23667326',
                'duracion_ms':391800,
                'tags':('Rock')
            },
            'Stardust Chords':{
                'liked':False,
                'reproducciones':16001476,
                'duracion_ms':274200,
                'tags':('Ballad')
            },
        }
    },
    'Stromae':{
        'Racine Carree':{
            'Ta Fete':{
                'liked':False,
                'reproducciones':75156132,
                'duracion_ms':'153000',
                'tags':('French Pop','Electro')
            },
            'Tous le Memes':{
                'liked':True,
                'reproducciones':194588900,
                'duracion_ms':198000,
                'tags':('French Pop','Electro')
            },
            'Ave Cesaria':{
                'liked':True,
                'reproducciones':'50747834',
                'duracion_ms':245400,
                'tags':('French Pop','Electro','Ethnic')
            }
        },
        'Multitude':{
            'Invaincu':{
                'liked':True,
                'reproducciones':'16732216',
                'duracion_ms':123000,
                'tags':('French Pop','Electro')
            },
            'Sante':{
                'liked':True,
                'reproducciones':'92011201',
                'duracion_ms':'186600',
                'tags':('Ethnic')
            },
            'Fils de Joie':{
                'liked':False,
                'reproducciones':'34948659',
                'duracion_ms':189000,
                'tags':('French Pop')
            },
        }
    },
}

#INDICACIONES
#NOTA:
'''
El diccionario provisto sigue la siguiente estructura
'Artista':{
        'Disco':{
            'Cancion':{
                'Si la Cancion nos gusta o no':False,
                'Cuantas reproducciones tiene':'397810130',
                'Cuanto Dura en milisegundos':187800,
                'Tags asociados':('Rock','Catchy Tunes')
            },
        }
    } 
'''
#1--- Imprimir el numero de reproducciones de la cancion "Highway Tune"
print(f"Reproducciones Highway TUne: {musica['Greta Van Fleet']['From the Fires']['Highway Tune']['reproducciones']}")

#2--- Imprimir el numero de reproducciones de la cancion "Heat Above"
print(f"Reproducciones Heat Above: {musica['Greta Van Fleet']['The Battle at Gardens Gate']['Heat Above']['reproducciones']}")

#3--- Imprimir la duracion de la cancion "Sante"
print(f"Duracion Sante: {musica['Stromae']['Multitude']['Sante']['duracion_ms']}ms")

#4--- Imprimir el segundo tag de la cancion "Lonely Boy"
print(f"SEgundo tag de Lonely Boy: {musica['The Black Keys']['El Camino']['Lonely Boy']['tags'][1]}")

#5--- Imprimir la duracion de la cancion "Little Black Submarines"
print(f"Duracion Little Black Submarines: {musica['The Black Keys']['El Camino']['Little Black Submarines']['duracion_ms']}ms")

#6--- Obtener la duracion total del disco "Multitude"
print(f"Duracion total de Multitude: {int(musica['Stromae']['Multitude']['Sante']['duracion_ms']) + musica['Stromae']['Multitude']['Invaincu']['duracion_ms'] + musica['Stromae']['Multitude']['Fils de Joie']['duracion_ms']}ms")

#7--- Obtener el promedio de reproducciones del disco "The Battle at Gardens Gate"
print(f"Promedio de reproducciones de The Battle at Gardens Gate: {(musica['Greta Van Fleet']['The Battle at Gardens Gate']['Heat Above']['reproducciones'] + int(musica['Greta Van Fleet']['The Battle at Gardens Gate']['Age of Machine']['reproducciones']) + musica['Greta Van Fleet']['The Battle at Gardens Gate']['Stardust Chords']['reproducciones'])/3}ms")

#8--- Obtener el numero de discos de The Black Keys y de Greta Van Fleet. Determinar quien tiene mas discos
print(f"Discos de The Black Keys: {len(musica['The Black Keys'])} discos")
print(f"Discos de Greta Van Fleet: {len(musica['Greta Van Fleet'])} discos")

#9--- Sustituir los tags de la cancion 'Little Black Submarines' por una tupla que contenga 
#     los valores unicos de la estructura original. Es decir, eliminar duplicados
musica['The Black Keys']['El Camino']['Little Black Submarines']['tags'] = tuple(set(musica['The Black Keys']['El Camino']['Little Black Submarines']['tags']))
print(f"Tags Little Black Submarines: {musica['The Black Keys']['El Camino']['Little Black Submarines']['tags']}")

#10--- Obtener la duracion promedio de las canciones del disco "Racine Carree"
print(f"Promedio de duracion de las canciones de Racine Carree: {(int(musica['Stromae']['Racine Carree']['Ta Fete']['duracion_ms']) + musica['Stromae']['Racine Carree']['Tous le Memes']['duracion_ms'] + musica['Stromae']['Racine Carree']['Ave Cesaria']['duracion_ms'])/3}ms")

#11--- Imprimir el nombre del disco con mas reproducciones de Greta Van Fleet
masreprodu = ""
temp1 = 0
for disco in musica['Greta Van Fleet']:
    temp=0
    for cancion in musica['Greta Van Fleet'][disco]:
        temp += int(musica['Greta Van Fleet'][disco][cancion]['reproducciones'])
        if temp > temp1:
            temp1 = temp
            masreprodu = disco
print(f"Disco con mas reproducciones de Greta Van Fleet: {masreprodu}")

#CANCELADO
#12--- Aniadir el tag "Cumbia" a la cancion "Sante"
lista=[]
lista.append(musica['Stromae']['Multitude']['Sante']['tags'])
lista.append("Cumbia")
musica['Stromae']['Multitude']['Sante']['tags']=lista
print(musica['Stromae']['Multitude']['Sante']['tags'])

#13--- Agregar la cancion "Tiene Espinas el Rosal" al disco "El Camino". La informacion de dicha cancion es la siguiente:
'''
'liked':True,
'reproducciones':'92011201',
'duracion_ms':'186600',
'tags':('Cumbion bien loco', 'Lo mejor para tus bodas')
'''
musica['The Black Keys']['El Camino']['Tiene Espinas el Rosal'] = {
'liked':True,
'reproducciones':'92011201',
'duracion_ms':'186600',
'tags':('Cumbion bien loco', 'Lo mejor para tus bodas')}
print(musica['The Black Keys']['El Camino']['Tiene Espinas el Rosal'])

#14--- Determinar cual es el disco con mas likes de todos, en caso de haber dos o mas discos con la misma cantidad de likes, imprime los dos discos
maslikes = ""
temp1 = 0
maslikes1=None
for artista in musica:
    for disco in musica[artista]:
        temp=0
        for cancion in musica[artista][disco]:
            if musica[artista][disco][cancion]['liked'] == True:
                temp += 1
                if temp > temp1:
                    temp1 = temp
                    maslikes = disco
                elif temp == temp1:
                    maslikes1 = disco
print(f"El disco con mas likes es = {maslikes}")
if maslikes1 != None:
    print(f"El segundo disco con mas likes es = {maslikes1}")
#si maslikes1 tiene un valor imprime hola
#15--- Determinar cual es el disco con mayor duracion de todos
masdura = ""
temp1 = 0
for artista in musica:
    for disco in musica[artista]:
        temp = 0
        for cancion in musica[artista][disco]:
            temp += int(musica[artista][disco][cancion]['duracion_ms'])
            if temp > temp1:
                temp1 = temp
                masdura = disco
print(f"El disco con mas duracion es = {masdura}")

#16--- Via consola, mostrar al usuario el nombre de los discos de  Greta Van Fleet. Pedirle al usuario que seleccione uno
#      una vez seleccionado, mostrar las canciones que lo componen. Pedir al usuario que seleccione una.
#      una vez seleccionada, preguntarle al usuario si le gustaria agregar un tag a la cancion. Si dice que si, determinar si el 
#      tag ya estaba presente en los tags. Si no estaba, agregarlo. Si ya estaba, imprimir "Hijole joven, no se va a poder"
#      imprimir la estructura resultante
f=1
for disco in musica['Greta Van Fleet']:
    print(f"{f}.- {disco}")
    f+=1
disco = int(input("Seleccione un disco (numero): "))
if(disco == 1):
    disco = "From the Fires"
    f=1
    for cancion in musica['Greta Van Fleet'][disco]:
        print(f"{f}.- {cancion}")
        f+=1
    cancion = int(input("Seleccione una cancion (numero): "))
    if(cancion == 1):
        cancion="Safari Song"
        print(cancion)
        des=input("Desea agregar un tag a la cancion? (si/no): ").upper()
        if(des=="SI"):
            tag=input("Ingrese el tag: ")
            if(tag in musica['Greta Van Fleet'][disco][cancion]['tags']):
                print("Hijole joven, no se va a poder")
            else:
                list=[musica['Greta Van Fleet'][disco][cancion]['tags']]
                list.append(tag)
                musica['Greta Van Fleet'][disco][cancion]['tags']=tuple(list)
                print(musica['Greta Van Fleet'][disco][cancion]['tags'])
        else:
            print("No se agregara ningun tag")
    elif(cancion==2):
        cancion="Edge of Darkness"
        print(cancion)
        des=input("Desea agregar un tag a la cancion? (si/no): ").upper()
        if(des=="SI"):
            tag=input("Ingrese el tag: ")
            if(tag in musica['Greta Van Fleet'][disco][cancion]['tags']):
                print("Hijole joven, no se va a poder")
            else:
                list=[musica['Greta Van Fleet'][disco][cancion]['tags']]
                list.append(tag)
                musica['Greta Van Fleet'][disco][cancion]['tags']=tuple(list)
                print(musica['Greta Van Fleet'][disco][cancion]['tags'])
        else:
            print("No se agregara ningun tag")
    elif(cancion==3):
        cancion="Highway Tune"
        print(cancion)
        des=input("Desea agregar un tag a la cancion? (si/no): ").upper()
        if(des=="SI"):
            tag=input("Ingrese el tag: ")
            if(tag in musica['Greta Van Fleet'][disco][cancion]['tags']):
                print("Hijole joven, no se va a poder")
            else:
                list=[musica['Greta Van Fleet'][disco][cancion]['tags']]
                list.append(tag)
                musica['Greta Van Fleet'][disco][cancion]['tags']=tuple(list)
                print(musica['Greta Van Fleet'][disco][cancion]['tags'])
        else:
            print("No se agregara ningun tag")
    elif(cancion==4):
        cancion="Black Smoke Rising"
        print(cancion)
        des=input("Desea agregar un tag a la cancion? (si/no): ").upper()
        if(des=="SI"):
            tag=input("Ingrese el tag: ")
            if(tag in musica['Greta Van Fleet'][disco][cancion]['tags']):
                print("Hijole joven, no se va a poder")
            else:
                list=[musica['Greta Van Fleet'][disco][cancion]['tags']]
                list.append(tag)
                musica['Greta Van Fleet'][disco][cancion]['tags']=tuple(list)
                print(musica['Greta Van Fleet'][disco][cancion]['tags'])
        else:
            print("No se agregara ningun tag")
elif(disco == 2):
    disco = "The Battle at Gardens Gate"
    f=1
    for cancion in musica['Greta Van Fleet'][disco]:
        print(f"{f}.- {cancion}")
        f+=1
    cancion = int(input("Seleccione una cancion (numero): "))
    if(cancion == 1):
        cancion="Heat Above"
        print(cancion)
        des=input("Desea agregar un tag a la cancion? (si/no): ").upper()
        if(des=="SI"):
            tag=input("Ingrese el tag: ")
            if(tag in musica['Greta Van Fleet'][disco][cancion]['tags']):
                print("Hijole joven, no se va a poder")
            else:
                list=[musica['Greta Van Fleet'][disco][cancion]['tags']]
                list.append(tag)
                musica['Greta Van Fleet'][disco][cancion]['tags']=tuple(list)
                print(musica['Greta Van Fleet'][disco][cancion]['tags'])
        else:
            print("No se agregara ningun tag")
    elif(cancion==2):
        cancion="Age of Machine"
        print(cancion)
        des=input("Desea agregar un tag a la cancion? (si/no): ").upper()
        if(des=="SI"):
            tag=input("Ingrese el tag: ")
            if(tag in musica['Greta Van Fleet'][disco][cancion]['tags']):
                print("Hijole joven, no se va a poder")
            else:
                list=[musica['Greta Van Fleet'][disco][cancion]['tags']]
                list.append(tag)
                musica['Greta Van Fleet'][disco][cancion]['tags']=tuple(list)
                print(musica['Greta Van Fleet'][disco][cancion]['tags'])
        else:
            print("No se agregara ningun tag")
    elif(cancion==3):
        cancion="Stardust Chords"
        print(cancion)
        des=input("Desea agregar un tag a la cancion? (si/no): ").upper()
        if(des=="SI"):
            tag=input("Ingrese el tag: ")
            if(tag in musica['Greta Van Fleet'][disco][cancion]['tags']):
                print("Hijole joven, no se va a poder")
            else:
                list=[musica['Greta Van Fleet'][disco][cancion]['tags']]
                list.append(tag)
                musica['Greta Van Fleet'][disco][cancion]['tags']=tuple(list)
                print(musica['Greta Van Fleet'][disco][cancion]['tags'])
        else:
            print("No se agregara ningun tag")
#EXTRA --- Estos no son a fuerza, pero si quieren un desafio y puntos extra valdria la pena intentarlo
#A--- Obtener el promedio de reproducciones del disco "The Battle at Gardens Gate" usando Ciclos For
promedio=0
for cancion in musica['Greta Van Fleet']['The Battle at Gardens Gate']:
    promedio+=int(musica['Greta Van Fleet']['The Battle at Gardens Gate'][cancion]['reproducciones'])
print(f"Promedio = {promedio/len(musica['Greta Van Fleet']['The Battle at Gardens Gate'])}")
#B--- Obtener la duracion total del disco "Multitude" usando Ciclos For
duracion=0
for cancion in musica['Stromae']['Multitude']:
    duracion+=int(musica['Stromae']['Multitude'][cancion]['duracion_ms'])
print(f"Duracion total Multitude = {duracion}")
#C--- Crear e imprimir una lista con los nombres de los Discos de Stroma usando List Comprehension
lista=[disco for disco in musica['Stromae']]
print(lista)