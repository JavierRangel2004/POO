series ={
    'Disney Plus':[
        {
            'The Mandalorian':{
                'temporadas':{
                    'Temporada 1':{
                        'episodios':'8',
                        'direccion':'El Cheems',
                        'calificacion':9.2,
                        'vistas':'32000000',
                        'tags':('star wars','filoniverse','dark saber')
                    },
                    'Temporada 2':{
                        'episodios':8,
                        'direccion':'Enrique Segoviano',
                        'calificacion':9.5,
                        'vistas':40000000,
                        'tags':('baby yoda','coursant','beskar')
                    }
                }
            }
        },
        {
            'The Bad Batch':{
                'temporadas':{
                    'Temporada 1':{
                        'episodios':'16',
                        'direccion':'El Canaca',
                        'calificacion':8.9,
                        'vistas':30000000,
                        'tags':('violencia animada','relleno')
                    },
                    'Temporada 2':{
                        'episodios':16,
                        'direccion':'El Canaca',
                        'calificacion':8.0,
                        'vistas':15000000,
                        'tags':('relleno','piu piu')
                    } 
                }
            }
        }
    ],
    'Netflix':[
        {
            'Dark':{
                'temporadas':{
                    'Temporada 1':{
                        'episodios':10,
                        'direccion':'Donald Trump',
                        'calificacion':9.5,
                        'vistas':20000000,
                        'tags':('such confusion','much time travel','wow')
                    },
                    'Temporada 2':{
                        'episodios':'8.0',
                        'direccion':'Donald Trump',
                        'calificacion':9.6,
                        'vistas':25500000,
                        'tags':('canciones ochenteras','spoiler')
                    },
                    'Temporada 3':{
                        'episodios':8,
                        'direccion':'Donald Trump',
                        'calificacion':9.7,
                        'vistas':'34000000',
                        'tags':('somos los malos?','best ending ever')
                    }
                }
            }
        },
        {
            '1899':{
                'temporadas':{
                    'Temporada 1':{
                        'episodios':8,
                        'direccion':'El Cheems',
                        'calificacion':9.5,
                        'vistas':40000000,
                        'tags':('cancelacion','misterio','barquitos')
                    }
                }
            }
        },
        {
            'Squid Game':{
                'temporadas':{
                    'Temporada 1':{
                        'episodios':9,
                        'direccion':'Calamardo Tentaculos',
                        'calificacion':9.5,
                        'vistas':60000000,
                        'tags':('violencia','jpop','cachetadas')
                    }
                }
            }
        }
    ],
    'HBO':[
        {
            'House of the Dragon':{
                'temporadas':{
                    'Temporada 1':{
                        'episodios':'10',
                        'direccion':'Viserys Targaryen',
                        'calificacion':9.5,
                        'vistas':40000000,
                        'tags':('acero valirio','dragones','reds vs greens')
                    }
                }
            }
        },
        {
            'The Last of Us':{
                'temporadas':{
                    'Temporada 1':{
                        'episodios':9,
                        'direccion':'Crash Bandicoot',
                        'calificacion':9.8,
                        'vistas':45000000,
                        'tags':('pan bimbo','hongos malos','terror')
                    }
                }
            }
        }
    ]
}

#Instrucciones
#Nota: Calculen promedios sin usar ciclos for, hagan las actividades en orden

#1) Obtener el promedio de vistas de todas las temporadas de la serie Dark
print(f"Promedio de vistas de todas las temporadas de la serie Dark = {(series['Netflix'][0]['Dark']['temporadas']['Temporada 1']['vistas']+series['Netflix'][0]['Dark']['temporadas']['Temporada 2']['vistas']+int(series['Netflix'][0]['Dark']['temporadas']['Temporada 3']['vistas']))/3}")
#usar ciclo for para el promedio
promedio = 0
for temporadas in series['Netflix'][0]['Dark']['temporadas']: 
    promedio +=int(series['Netflix'][0]['Dark']['temporadas'][temporadas]['vistas'])
print(f"Promedio de vistas de todas las temporadas de la serie Dark = {promedio/len(series['Netflix'][0]['Dark']['temporadas'])}")

#2) Obtener el promedio de calificacion de todas las temporadas de la serie The Mandalorian
print(f"Promedio de calificacion de todas las temporadas de la serie The Mandalorian = {(series['Disney Plus'][0]['The Mandalorian']['temporadas']['Temporada 1']['calificacion']+series['Disney Plus'][0]['The Mandalorian']['temporadas']['Temporada 2']['calificacion'])/2}")

#3) Obtener el primer tag de la temporada 1 de The Last of Us
print(f"Primer tag Last Of Us = {series['HBO'][1]['The Last of Us']['temporadas']['Temporada 1']['tags'][0]}")

#4) Obtener el numero de series emitidas por Disney Plus
print(f"Series Disney = {len(series['Disney Plus'])}")

#5) Obtener nombre del director de la primera temporada de The Mandalorian
print(f"Director mandalorian = {series['Disney Plus'][0]['The Mandalorian']['temporadas']['Temporada 1']['direccion']}")

#6) Obtener el numero de series emitidas por Netflix
print(f"Series Disney = {len(series['Netflix'])}")

#7) Obtener el tercer tag de la temporada 1 de Squid Game
print(f"Tercer tag SquidGame = {series['Netflix'][2]['Squid Game']['temporadas']['Temporada 1']['tags'][2]}")

#8) Obtener nombre del director de la primera temporada de Squid Game
print(f"Director SquidGame = {series['Netflix'][2]['Squid Game']['temporadas']['Temporada 1']['direccion']}")

#9) Obtener nombre del director de la segunda temporada de The Mandalorian
print(f"Director mandalorian = {series['Disney Plus'][0]['The Mandalorian']['temporadas']['Temporada 2']['direccion']}")

#10) Cambiar el segundo tag de la temporada 1 de The Last of Us por "hongos buenos"
series['HBO'][1]['The Last of Us']['temporadas']['Temporada 1']['tags']=list(series['HBO'][1]['The Last of Us']['temporadas']['Temporada 1']['tags'])
series['HBO'][1]['The Last of Us']['temporadas']['Temporada 1']['tags'][1]='hongos buenos'

#11) Cambiar el segundo tag de la temporada 1 de Squid Game por "kpop"
series['Netflix'][2]['Squid Game']['temporadas']['Temporada 1']['tags']=list(series['Netflix'][2]['Squid Game']['temporadas']['Temporada 1']['tags'])
series['Netflix'][2]['Squid Game']['temporadas']['Temporada 1']['tags'][1]='kpop'

#12) Cambiar la calificion de la tercr temporada de dark a 10
series['Netflix'][0]['Dark']['temporadas']['Temporada 3']['calificacion']=10

#13) Obtener el promedio de calificaciones de todas las temporadas de la serie Dark
print(f"Promedio calis. Dark = {(series['Netflix'][0]['Dark']['temporadas']['Temporada 1']['calificacion']+series['Netflix'][0]['Dark']['temporadas']['Temporada 2']['calificacion']+series['Netflix'][0]['Dark']['temporadas']['Temporada 3']['calificacion'])/3}")

#14) Via consola, pedir al usuario que escriba un tag con el que le gustaria calificar la primer temporada de House of the Dragon.
#Si el tag ya existe dentro de los tags, indicar al usuario que dicho tag ya existe e imprimir la estructura
#correspondiente. Si el tag no existe, preguntar al usuario si desearia agregar dicho tag a la estructura.
#Si el usuario selecciona "Si" agregar el tag, si selecciona "No" imprimir "ta bueno pues"
#Imprimir la estrucutra final
tagnuevo=input('Escribe un tag con el que le gustaria calificar la primer temporada de House of the Dragon: ')
if (tagnuevo in series['HBO'][0]['House of the Dragon']['temporadas']['Temporada 1']['tags']):
    print(f"Ya esta - {series['HBO'][0]['House of the Dragon']['temporadas']['Temporada 1']['tags']}")
elif (tagnuevo not in series['HBO'][0]['House of the Dragon']['temporadas']['Temporada 1']['tags']):
    print('El tag no existe')
    respuesta=input('¿Desea agregar el tag? (Si/No): ').upper()
    if (respuesta=='SI'):
        series['HBO'][0]['House of the Dragon']['temporadas']['Temporada 1']['tags']+=tagnuevo,
        print(f"Tag agregado = {series['HBO'][0]['House of the Dragon']['temporadas']['Temporada 1']['tags']}")
    else:
        print('Ta bueno pues')

#15 via consola, el usuario debe ingresar los campos que compondran la temporada 2 de the last of us.
#La consola debe pedir al usuario el numero de episodios, el nombre del director, la calificacion,
#las vistas y una tag. Aniadir estos datos a la estructura correspondiente. Al final, imprimir el diccionario completo
#El resultado debe verse mas  o menos asi:
#RECUERDEN COMO SE AGREGAN KEYS A UN DICCIONARIO GUINIO GUINIO
'''
'The Last of Us':{
                'temporadas':{
                    'Temporada 1':{
                        **Estos datos ya estan comododados
                    },
                    'Temporada 2':{
                        **Aqui van los datos recolectados via consola
                    }
                }
'''
episodios=int(input('Numero de episodios: '))
director=input('Nombre del director: ')
calificacion=float(input('Calificacion: '))
vistas=int(input('Vistas: '))
tag=input('Tag: ')
series['HBO'][1]['The Last of Us']['temporadas']['Temporada 2']={'episodios':episodios,'direccion':director,'calificacion':calificacion,'vistas':vistas,'tags':tag}
print(series['HBO'][1]['The Last of Us']['temporadas']['Temporada 2'])
