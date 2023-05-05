def nombre_apellido(nombre):
    import openai
    openai.api_key = "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"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a chatbot"},
            {"role": "user", "content": f"{nombre}, separa el anterior nombre con el siguiente formato: 'nombre': <nombres>, 'apellidos': <apellidos>"},
            #Ernesto Gabriel Fernando Lopez, regresame una lista de python con el siguiente formato: ["nombres","apellidos"] (no quiero un codigo, solo quiero la lista de regreso)
        ]
    )
    result = ''
    for choice in response.choices:
        result += choice.message.content
    print(result)
import os
def clear():
    input("Presiona enter para continuar...")
    os.system('clear')

Pruebas= ['Javier Alejandro Rangel Murillo','Ernesto Gabriel Fernando Lopez','Diego Jose Vitela','Luis Cedillo Maldonado', 'Melany De la Cruz Toscano', 'Juan Esteban Mayoral Zepeda', 'Emiliano del Jesus Lopez', 'Mónica Patricia de Ávalos Mendoza', 'Gabriela de la Pava de la Torre', 'Juan Fernando Pérez del Corral', 'Valentina Laverde de la Rosa', 'Óscar de la Renta', 'Sara Teresa Sánchez del Pinar', 'Efraín de las Casas Mejía', 'Julieta Ponce de León', 'Martín Elías de los Ríos Acosta', 'Gabriela de la Pava de la Torre', 'Matías de Greiff Rincón', 'Manuela del Pino Hincapié', 'Sebastián del Campo Yepes', 'Sofía del Río Arango', 'Ana María de la Peña Posada', 'Mónica Patricia de Ávalos Mendoza']

for nombre in Pruebas:
    print(nombre)
    nombre_apellido(nombre)
    clear()