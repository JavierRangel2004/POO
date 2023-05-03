def duraciones(**disco):
    dur=0
    if len(disco)==0:
        raise(Exception("El disco no tiene canciones"))
    for cancion in disco:
        dur+=disco[cancion]['duracion_ms']
    return dur