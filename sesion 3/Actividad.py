nom=input("Ingresa tu nombre: ")
edad=int(input("Ingresa tu edad: "))
dia=int(input("Ingresa dia de nacimiento: "))
mes=int(input("Ingresa mes de nacimiento: "))
año=int(input("Ingresa año de nacimiento: "))
cp=int(input("Ingresa tu codigo postal: "))
curp=input("Ingresa tu CURP: ")
folio=dia*mes*año*cp
print(f"Hola {nom.upper()},\nFecha de nacimiento: {dia}/{mes}/{año}\nEdad: {edad}\nCodigo Postal: {cp}\nCURP: {curp.upper()}\nCon estos datos tu folio es: {folio}")