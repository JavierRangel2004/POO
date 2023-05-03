Mi_diccionario={
    "nombre":"Javier"
}
print(Mi_diccionario)
#añadir valor a un diccionario hacer como que ya existe
Mi_diccionario["tipo de sangre"]="O+"
print(Mi_diccionario)
print(Mi_diccionario.items())
for llave,valor in Mi_diccionario.items():
    print(f"La llave es {llave}. \nEl valor es: {valor}")