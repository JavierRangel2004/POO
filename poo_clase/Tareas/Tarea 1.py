videojuegos = {
    'Epic Games':[
        {
            'Gears of War 3':{
                'genero':'FPS',
                'anio':2011,
                'calificacion':9,
                'ventas mundiales':3000000,
                'tags':['disparos','gore','violencia bien intensa'],
                'equipo':{
                    'Lead Designer':'El Cheems',
                    'Art Director':'La Cholondrina'
                }
            }
        },
        {   
            'Gears Tactics':{
                'genero':'Strategy',
                'anio':2019,
                'calificacion':9,
                'ventas mundiales':'1500000',
                'tags':('gore estrategico','gore','violencia bien intensa'),
                'equipo':{
                    'Lead Designer':'El Cheems',
                    'Art Director':'La Cholondrina'
                }
            }
        },
        {
               'Fortnite':{
                'genero':'Battle Royale',
                'anio':2017,
                'calificacion':'9',
                'ventas mundiales':30000000,
                'tags':['niños rata','microtransacciones','disparos'],
                'equipo':{
                    'Lead Designer':'El Medio Metro',
                    'Art Director':'Alfredo Adame'
                }
            }
        }
    ],
    '343 Industries':[
        {
            'Halo Infinite':{
                'genero':'FPS',
                'anio':2020,
                'calificacion':9,
                'ventas mundiales':'4000000',
                'tags':('disparos','aliens','microtransacciones'),
                'equipo':{
                    'Lead Designer':'Maestr Cheef',
                    'Art Director':'Bob Ross'
                }
            }
        },
        {
            'Halo Wars 2':{
                'genero':'Strategy',
                'anio':2017,
                'calificacion':7,
                'ventas mundiales':100000,
                'tags':('estrategia','wololo','the banished'),
                'equipo':{
                    'Lead Designer':'Gerard Pique',
                    'Art Director':'Salgado Macedonio'
                }
            }
        }
    ],
    'Ubisoft':[
        {
            'Assassins Creed: Valhalla':{
                'genero':'RPG',
                'anio':2020,
                'calificacion':9,
                'ventas mundiales':2000000,
                'tags':('vikingos','canciones de vikingos','violencia de vikingos'),
                'equipo':{
                    'Lead Designer':'Beakman',
                    'Art Director':'Pingu el Pinguino'
                }
            }
        },
        {   
            'Avatar: Frontiers of Pandora':{
                'genero':'RPG',
                'anio':2022,
                'calificacion':0,
                'ventas mundiales':0,
                'tags':('magia naturistica','aventuras espaciales','violencia de pitufos'),
                'equipo':{
                    'Lead Designer':'James Hetfield',
                    'Art Director':'Rick Roll'
                }
            }
        }
    ],
    'CD Projekt Red':[
        {
            'Cybepunk 2077':{
                'genero':'RPG',
                'anio':2020,
                'calificacion':7,
                'ventas mundiales':3000000,
                'tags':('disparos','mucho neon bling bling','violencia del futuro'),
                'equipo':{
                    'Lead Designer':'Spoderman',
                    'Art Director':'Hasbulla'
                }
            }
        },
        {
            'Red Dead Redemption II':{
                'genero':'Adventure',
                'anio':2018,
                'calificacion':9,
                'ventas mundiales':46000000,
                'tags':('disparos','vaqueros','violencia con caballos'),
                'equipo':{
                    'Lead Designer':'Abdu Rozik',
                    'Art Director':'Mamberoy'
                }
            }
        },
        {
            'The Witcher III':{
                'genero':'RPG',
                'anio':2015,
                'calificacion':9,
                'ventas mundiales':40000000,
                'tags':('magia muy magica','violencia','fantasia'),
                'equipo':{
                    'Lead Designer':'Warren Buffet',
                    'Art Director':'El Escorpion Dorado'
                }
            }
        }
    ]
}

#INDICACIONES
#1 Imprimir el nombre del Lead Designer de Gears of War 3
print(videojuegos['Epic Games'][0]['Gears of War 3']['equipo']['Lead Designer'])

#2 Imprimir el nombre del Art Director de Cybepunk 2077
print(videojuegos['CD Projekt Red'][0]['Cybepunk 2077']['equipo']['Art Director'])

#3 Imprimir el number de ventas mundiales de Assassins Creed: Valhalla
print(videojuegos['Ubisoft'][0]['Assassins Creed: Valhalla']['ventas mundiales'])

#4 Imprimir el segundo tag de Cybepunk 2077
print(videojuegos['CD Projekt Red'][0]['Cybepunk 2077']['tags'][1])

#5 Calcular el numero de ventas totales de los juegos de 343 Industries
print(f"Numero de ventas mundiales 343 Industries: {videojuegos['343 Industries'][1]['Halo Wars 2']['ventas mundiales']+int(videojuegos['343 Industries'][0]['Halo Infinite']['ventas mundiales'])}")

#6 Calcular el promedio de calificaciones de juegos de CD Projekt Red
print(f"Promedio de calificaciones de CD Projekt Red: {(videojuegos['CD Projekt Red'][0]['Cybepunk 2077']['calificacion']+videojuegos['CD Projekt Red'][1]['Red Dead Redemption II']['calificacion']+videojuegos['CD Projekt Red'][2]['The Witcher III']['calificacion'])/3}")

#7 Imprimir el numero de tags que tiene Fortnite
print(f"Tags de fortnite = {len(videojuegos['Epic Games'][2]['Fortnite']['tags'])}")
#8 Añadir el Tag "Juego de los God" a Gears of War 3
videojuegos['Epic Games'][0]['Gears of War 3']['tags'].append("Juego de los God")
print(videojuegos['Epic Games'][0]['Gears of War 3']['tags'])
#9 Cambiar el tag "aliens" de Halo infinite por "Espartans"
videojuegos['343 Industries'][0]['Halo Infinite']['tags']=list(videojuegos['343 Industries'][0]['Halo Infinite']['tags'])
videojuegos['343 Industries'][0]['Halo Infinite']['tags'][1]="Espartans"
print(videojuegos['343 Industries'][0]['Halo Infinite']['tags'])
#10 Añadir a "Juan Gabriel" como Music Director de 'Red Dead Redemption II' *recuerden como se crean keys nuevas en diccionarios
videojuegos['CD Projekt Red'][1]['Red Dead Redemption II']['equipo']['Music Director']="Juan Gabriel"
print(videojuegos['CD Projekt Red'][1]['Red Dead Redemption II']['equipo'])