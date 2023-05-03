alumno = {
    "nombre": "Amapolo",
    "edad": 23,
    "situacion": "regular",
    "hobbies": ["nadar", "correr", "hacer el paso del pinguino"],
    "materias": {
        "historia": {
            "profesor": {
                "nombre": "Juan Carlos Bodoque",
                "universidad": "UNAM",
                "año egreso": 1982
            },
            "calificacion": "10"
        },
        "algebra": {
            "profesor": {
                "nombre": "Salgado Macedonio",
                "universidad": "SINATRACA",
                "año egreso": 1988
            },
            "calificacion": "7.2"
        },
        "programacion": {
            "profesor": {
                "nombre": "Peter Parker",
                "universidad": "IPN",
                "año egreso": 2012
            },
            "calificacion": "8.9"
        },
    }
}
#Imprimir el nombre y la edad del alumno -> El alumno X tiene Y años
print(f"El alumno {alumno['nombre']} tiene {alumno['edad']} años.")

#Imprimir el tercer hobby del alumno
print(f"Su tercero hobby: {alumno['hobbies'][2]}")

#Obtener el promedio del alumno
print(f"Su promedio es de: {((float(alumno['materias']['historia']['calificacion']))+(float(alumno['materias']['algebra']['calificacion']))+(float(alumno['materias']['programacion']['calificacion'])))/3}")


#Indicar el nombre, institución y año de egreso del profesor de programación
#El profesor X egresó en Y del Z
print(f"El profesor {alumno['materias']['programacion']['profesor']['nombre']} egresó en {alumno['materias']['programacion']['profesor']['año egreso']} del {alumno['materias']['programacion']['profesor']['universidad']}")

#Cambiar el tercer hobby del alumno por “ir a misa”
alumno["hobbies"][2]="ir a misa"
print(f"Su nuevo tercero hobby: {alumno['hobbies'][2]}")

#Cambiar la calificación de algebra a 9.2
alumno["materias"]["algebra"]["calificacion"]=9.2
print(f"Nueva cali algebra: {alumno['materias']['algebra']['calificacion']}")

#Obtener el promedio del alumno
print(f"Nuevo promedio: {((float(alumno['materias']['historia']['calificacion']))+(float(alumno['materias']['algebra']['calificacion']))+(float(alumno['materias']['programacion']['calificacion'])))/3}")

#Cambiar el nombre, institución y año de egreso del profesor de programacion
alumno["materias"]["programacion"]["profesor"]["nombre"]="Albus Dumbledore"
alumno["materias"]["programacion"]["profesor"]["universidad"]="Universidad Panamerica"
alumno["materias"]["programacion"]["profesor"]["año egreso"]=1865
print(f"El nuevo profesor {alumno['materias']['programacion']['profesor']['nombre']} egresó en {alumno['materias']['programacion']['profesor']['año egreso']} del {alumno['materias']['programacion']['profesor']['universidad']}")