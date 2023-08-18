import turtle
import time
import random

delay = 0.1
segmentos = []
score = 0
score_historico = 0

# Ventana
ventana = turtle.Screen()
ventana.setup(width=600, height=600)
ventana.title("Snake")
ventana.bgcolor("black")

# Serpiente settings
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direction = "stop"

# Comida settings
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0, 100)
comida.direction = "stop"

# Score
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write(f"Score: 0       High Score: 0", align="center", font=("Arial", 24))


# Movimiento de la serpiente
def movimiento():
    """Almacenar el valor actual de la coordenada"""
    y = cabeza.ycor()
    x = cabeza.xcor()
    if cabeza.direction == "up":
        cabeza.sety(y + 10)
    if cabeza.direction == "down":
        cabeza.sety(y - 10)
    if cabeza.direction == "right":
        cabeza.setx(x + 10)
    if cabeza.direction == "left":
        cabeza.setx(x - 10)
        
def dir_arriba():
    if cabeza.direction != "down":
        cabeza.direction = "up"
def dir_abajo():
    if cabeza.direction != "up":
        cabeza.direction = "down"
def dir_derecha():
    if cabeza.direction != "left":
        cabeza.direction = "right"
def dir_izquierda():
    if cabeza.direction != "right":
        cabeza.direction = "left"
                
# Conectar teclado    
ventana.listen()
ventana.onkeypress(dir_arriba, "Up")
ventana.onkeypress(dir_abajo, "Down")
ventana.onkeypress(dir_derecha, "Right")
ventana.onkeypress(dir_izquierda, "Left") 
  
      
# Reiniciar juego
def reiniciar_juego():
        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direction = "stop"
        # Eliminar segmentos
        for seg in segmentos:
            seg.goto(1000, 1000)
        segmentos.clear()

# Score
def actualizar_score():
    global score, score_historico
    texto.clear()
    texto.write(f"Score: {score}       High Score: {score_historico}", align="center", font=("Arial", 24))

while True:
    ventana.update()
    
    # colisión con la comida
    if cabeza.distance(comida) <20:
        x = random.randint(-280, 280)
        y = random.randint (-280, 280)
        comida.goto(x, y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("gray")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)
        
        score += 10
        if score > score_historico:
            score_historico = score
        actualizar_score()
    total_segmentos = len(segmentos)   
    
    # Se obtienen las coordenadas del segmento anterior y se asignan al segmento actual
    for i in range(total_segmentos -1, 0, -1):
        x = segmentos[i-1].xcor()
        y = segmentos[i-1].ycor()
        segmentos[i].goto(x, y)
    # Si hay segmentos se mueven a la posicion de la cabeza    
    if total_segmentos:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)
        
    # Colision con la ventana
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        reiniciar_juego()
        score = 0
        actualizar_score()
       
    movimiento()
    # Colision con el propio cuerpo
    for seg in segmentos:
        if seg.distance(cabeza) < 10:
            reiniciar_juego()
            score = 0
            actualizar_score()
      
    time.sleep(delay)


turtle.done()
