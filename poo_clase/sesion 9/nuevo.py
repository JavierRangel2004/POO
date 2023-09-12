alumnos=[
    {
        'nombre':'EL cheems',
        'calificacion':89
    },
    {
        'nombre':'medio metro',
        'calificacion':70
    },
    {
        'nombre':'Chabelo',
        'calificacion':100
    }
]
#DERROTA

# temp=0
# for i in alumnos:
#     for j,h in i.items():
#         if(type(h)==int):
#             temp+=h
# print (f"Promedio= {temp/len(alumnos)}")

temp=0
for dicc in alumnos:
    temp+=dicc['calificacion']
print (f"Promedio= {temp/len(alumnos)}")

nombres=[i['nombre'] for i in alumnos]
print (nombres)
