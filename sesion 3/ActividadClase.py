letra="""A mí me gusta el Tangananica
Y yo prefiero el tanganana
La mejor frase es tangananica
El mejor verso es tanganana
Tangananica-nica-nica-nica
Tanganana
Todo lo explica, no explica na'
Para alegrarme digo tangananica
Para reírme digo tanganana
Comí un rico tangananica
A mí me dieron tanganana
Tangananica-nica-nica-nica
Tanganana
Me tienes pica, pica, pica, pica
No pasa na'
Como voy a perder, mi palabra es tan buena
Tu palabra es tan mala, no hay nada que hacer
Como vas a ganar si la mejor palabra es tanganana
Tú siempre dices tangananica
Tú siempre gritas tanganana
Ya no soporto el tangananica
Y yo detesto tu tanganana
Tangananica-nica-nica-nica
Tanganana
Nuestra mamá nos va a retar
Ordenemos mejor o sí
Después nos vamos"""
print(letra.lower())
letra=letra.lower().replace("tangananica","tacos de chistorra").replace("tanganana","los tlacoyos frios")
print(letra)
print(f"Tangananica cambio {letra.count('los tlacoyos frios')} veces a tacos de chistorra")
print(f"Tanganana cambio {letra.count('tacos de chistorra')} veces a los tlacoyos frios")