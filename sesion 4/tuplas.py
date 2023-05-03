#la tupla no se puede modificar
calis=(7,2,3,6,5)
print(calis)
calis=list(calis)
calis[0]="tuputamadre"
calis=tuple(calis)
print(calis)