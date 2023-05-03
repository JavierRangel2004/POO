canales = {
    "Star Channel":{
        "series":{
            "Los Simpson":{
                "año de creacion":1989,
			    "temporadas":32,
			    "capitulos":692,
                "tags":("Comedia","Violencia","Romance"),
			    "calificacion":6,
			    "creador":{
                    "nombre":"Cosme Fulanito",
                    "nacionalidad": "Wakandiano"
                }
            }
        }
    },
    "Comedy Central":{
        "series":{
            "The Office":{
                "año de creacion":2005,
			    "temporadas":9,
			    "capitulos":188,
                "tags":("Comedia","Accion","Aventura"),
			    "calificacion":"8",
			    "creador":{
                    "nombre":"Greg Daniels",
                    "nacionalidad": "Americano"
                }
            },
            "South Park":{
                "año de creacion":1997,
			    "temporadas":23,
			    "capitulos":307,
                "tags":("Comedia","Violencia","Desnudos"),
			    "calificacion":9,
			    "creador":{
                    "nombre":"Trey Parker",
                    "nacionalidad": "Americano"
                }
            }

        }
    },
    "Warner":{
         "series":{
            "The Big Bang Theory":{
                "año de creacion":2007,
			    "temporadas":12,
			    "capitulos":279,
                "tags":("Romance","Violencia"),
			    "calificacion":8,
			    "creador":{
                    "nombre":"Chuck Lorre",
                    "nacionalidad": "Americano"
                }
            },
            "Two and a Half Men":{
                "año de creacion":2003,
			    "temporadas":12,
			    "capitulos":"262",
                "tags":("Aventura","Romance","Musical"),
			    "calificacion":7,
			    "creador":{
                    "nombre":"Chuck Lorre",
                    "nacionalidad": "Americano"
                }
            }
        }
    },
    "Adult Swim":{
         "series":{
            "Rick Y Morty":{
                "año de creacion":2013,
			    "temporadas":4,
			    "capitulos":41,
                "tags":("Romance"),
			    "calificacion":9,
			    "creador":{
                    "nombre":"Justin Roiland",
                    "nacionalidad": "Americano"
                }
            }         
        }
    }
}

#Cambiar el nombre y nacionalidad del creador de los Simpson de Comse Fulatino a Matt Groening y de Wakandiano a Americano
canales['Star Channel']['series']['Los Simpson']['creador']['nombre']="Matt Groening"
canales['Star Channel']['series']['Los Simpson']['creador']['nacionalidad']="Americano"
print(canales['Star Channel']['series']['Los Simpson']['creador'])
#Comparar el numero de episodios de la teoria del big bang vs two and a half man. Usen operadores booleanos
if(canales['Warner']['series']['The Big Bang Theory']['capitulos']>int(canales['Warner']['series']['Two and a Half Men']['capitulos'])):
    capi=True
else:
    capi=False
print(f"The big bang theory tiene mas episodios: {capi}")

#En Southpark, cambiar el tag de "Desnudos" por "Contenido Educativo"
canales['Comedy Central']['series']['South Park']['tags']=list(canales['Comedy Central']['series']['South Park']['tags'])
canales['Comedy Central']['series']['South Park']['tags'][2]="Contenido Educativo"

canales['Comedy Central']['series']['South Park']['tags']=tuple(canales['Comedy Central']['series']['South Park']['tags'])
print(canales['Comedy Central']['series']['South Park']['tags'])

#En los tags de Los Simpson buscar "Violencia". Si está presente, imprimir TRUE. usar operadores booleanos, no usar IF
print("Violencia"in canales['Star Channel']['series']['Los Simpson']['tags'])

#Indicar la suma de capitulos de las series de Warner
print(f"Total capitulos Warner = {canales['Warner']['series']['The Big Bang Theory']['capitulos']+int(canales['Warner']['series']['Two and a Half Men']['capitulos'])}")

#Crear una nueva key en el diccionario de series de 
# Adult Swim para la serie 
# "Celebrity Deathmatch con los siguientes valores:
'''
"año de creacion":1998,
	"temporadas":6,
	"capitulos":93,
	"calificacion":9,
	"creador":{
        "nombre":"Eric Fogel",
        "nacionalidad": "Americano"
    }
'''
canales["Adult Swim"]['Celebrity Deathmatch']={
    "año de creacion":1998,
	"temporadas":6,
	"capitulos":93,
	"calificacion":9,
	"creador":{
        "nombre":"Eric Fogel",
        "nacionalidad": "Americano"
    }

}
print(canales["Adult Swim"]['Celebrity Deathmatch'])

# Obtener el promedio de calificaciones de las series de Warner.
print(f"Promedio de calificaión de Warner = {(canales['Warner']['series']['The Big Bang Theory']['calificacion']+canales['Warner']['series']['Two and a Half Men']['calificacion'])/2}")

# Imprimir TRUE Si el promedio es menor a 7. Usen operadores booleanos, no usar IF
print(((canales['Warner']['series']['The Big Bang Theory']['calificacion']+canales['Warner']['series']['Two and a Half Men']['calificacion'])/2)<7)