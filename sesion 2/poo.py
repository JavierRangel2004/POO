nom=input("Ingresa tu nombre: ")
n=int(input("Ingresa cantidad de actividades: "))
act_l=""
dur_l=0
act_c=""
dur_c=25
for i in range(n):
  act=(input("Ingresa nombre de la actividad: "))
  dur=float(input("Ingresa duración de la actividad: "))
  if (dur<dur_c):
    dur_c=dur
    act_c=act
  if(dur>dur_l):
    dur_l=dur
    act_l=act
print(f"Hola {nom}.\nLa actividad que tarda más tiempo es: {act_l}\nLa tarea que tarda menos tiempo es: {act_c}")
#print("hola mundo")