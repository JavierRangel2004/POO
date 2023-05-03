import requests
import os
import pandas as pd
'''
urlbase='https://hp-api.onrender.com/api/'
response=requests.get(url=f"{urlbase}spells")
response
diccionario_hechizos=response.json()
print(type(diccionario_hechizos))
for cosa in diccionario_hechizos:
    print(type(cosa))
'''
def clear():
    input("Presiona Enter para continuar...")
    os.system('cls')

class hpAPI():
    def __init__(self):
        print("Objeto creado")
        self.urlbase='https://hp-api.onrender.com/api/'

    def personajes(self):
        response=requests.get(f"{self.urlbase}characters")
        return pd.DataFrame(response.json())
    
    def hechizos(self):
        return(requests.get(f"{self.urlbase}spells")).json()
    
    def buscar_h(self,spell):
        cont=1
        found=False
        for hechizo in self.hechizos():
            if spell.capitalize()==hechizo['name']:
                found=True
                print(f"{cont}.- {hechizo['name']}")
            cont+=1
        if found==False:
            print("404: Spell not found")

    def char_house(self,house):
        return(requests.get(f"{self.urlbase}characters/house/{house}")).json()
    
HarryPotter=hpAPI()
HarryPotter.personajes()
#HarryPotter.personajes().to_csv('resultado.csv',index=False)

# clear()
# print(HarryPotter.hechizos())
# clear()
# spell=input("Spell to search: ")
# HarryPotter.buscar_h(spell)
# clear()
# print(HarryPotter.char_house('slytherin'))