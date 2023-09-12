import funciones
alumno={
    'nombre':'Javier',
    'edad':18,
    'nacionalidad':'MX'
}

funciones.info_user(**alumno)

grados=int(input("Ingresa num de grados: "))
print(f"Grados ingresados a farenheit: {funciones.farenheit(grados)}")