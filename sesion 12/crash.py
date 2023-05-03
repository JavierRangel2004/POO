pasosMedioMetro=['del pinguino','el cabeceo','corazon']
if 'el caballo'not in pasosMedioMetro:
    pasosMedioMetro.append('el cabllo')
    #raise(ValueError("El paso no esta pero se agrego"))

while(True):
    edad =input("Cual es tu edad: ")
    try:
        print(f"Tu edad en 20 años sera {int(edad)+20}")
        break
    except:
        print("Eso no es numero.")
