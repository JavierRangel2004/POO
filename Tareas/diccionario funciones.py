#Crear una funcion que permita calcular el total de duracion de cada disco.
#Cada disco sera presentado como su propio diccionario
#El promedio debe ser calculado usando ciclos for
#Testear la funcion con los siguientes 3 diccionarios:
import os
from funciones import duraciones
El_Camino ={
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

From_the_Fires={
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
        }

Racine_Carree={
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
}
MedioMetro={
}

#Una vez se tenga lista la funcion, separarla del archivo principal de manera que pueda ser llamada
#desde otro archivo usando el alias "promedio"
os.system('cls')
print(f"Duracion el Camino = {duraciones(**El_Camino)} ms")
print(f"Duracion el Camino = {duraciones(**MedioMetro)} ms")