

message="""
Días disponibles:
1) Thursday 02 November 17:30-18:00
2) Friday 03 November 17:30-18:00
3) Wednesday 08 November 17:00-17:30
4) Wednesday 08 November 17:30-18:00
5) Thursday 09 November 17:00-17:30
"""

def translate_message(message):
    #check if there are words in english and translate them to spanish
    dict_word={
        "Monday":"Lunes",
        "Tuesday":"Martes",
        "Wednesday":"Miércoles",
        "Thursday":"Jueves",
        "Friday":"Viernes",
        "January":"Enero",
        "February":"Febrero",
        "March":"Marzo",
        "April":"Abril",
        "May":"Mayo",
        "June":"Junio",
        "July":"Julio",
        "August":"Agosto",
        "September":"Septiembre",
        "October":"Octubre",
        "November":"Noviembre",
        "December":"Diciembre",
    }

    words = message.split()
    for word in words:
        if word in dict_word:
            message = message.replace(word, dict_word[word])

    return message

print(translate_message(message))