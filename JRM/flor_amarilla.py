import turtle

def dibujar_girasol():
    # Configuración de la ventana
    ventana = turtle.Screen()
    ventana.bgcolor("white")
    
    # Crear una tortuga para dibujar
    t = turtle.Turtle()
    t.speed(10)  # Velocidad de dibujo

    # Dibujar el mensaje "Te amo Luis" en la parte superior
    t.penup()
    t.goto(0, 250)
    t.write("Te amo Luis", align="center", font=("Arial", 24, "bold"))
    t.pendown()

    # Dibujar el centro del girasol (amarillo-café)
    t.color("yellow", "saddlebrown")
    t.begin_fill()
    t.circle(50)
    t.end_fill()

    # Dibujar los pétalos amarillos
    t.color("yellow")
    for _ in range(12):
        t.forward(70)
        t.circle(10, 60)
        t.circle(20, 60)
        t.backward(70)
        t.right(30)

    # Dibujar el tallo verde
    t.color("green")
    t.right(90)
    t.forward(200)

    # Dibujar las hojas amarillas
    t.color("yellow")
    t.circle(50, 60)
    t.circle(20, 60)
    t.backward(70)
    t.left(120)
    t.circle(50, 60)
    t.circle(20, 60)
    t.backward(70)

    # Finalizar el dibujo
    turtle.done()

# Llamar a la función para dibujar el girasol
dibujar_girasol()
