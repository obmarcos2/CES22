import turtle

turtle.setup(800, 600)
wn = turtle.Screen()
wn.title("Tess.")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shapesize(2)

def turn_red():
    tess.fillcolor("red")
def turn_green():
    tess.fillcolor("green")
def turn_blue():
    tess.fillcolor("blue")

def inc_pen():
    a = tess.pensize()
    if (a+1) > 20:
        tess.pensize(20)
    else:
        tess.pensize(a+1)
def dec_pen():
    a = tess.pensize()
    if (a-1) < 1:
        tess.pensize(1)
    else:
        tess.pensize(a-1)

def forward():
    tess.forward(5)
def backward():
    tess.back(5)
def left():
    tess.left(10)
def right():
    tess.right(10)

s = 0

def pen_attribute():
    global s
    if s == 0:
        tess.penup()
        s = 1
        return
    if s == 1:
        tess.pendown()
        s = 0

wn.onkey(turn_red, "r")
wn.onkey(turn_blue, "b")
wn.onkey(turn_green, "g")
wn.onkey(inc_pen, "KP_Add")
wn.onkey(dec_pen, "KP_Subtract")
wn.onkey(forward, "w")
wn.onkey(backward, "s")
wn.onkey(left, "a")
wn.onkey(right, "d")
wn.onkey(pen_attribute, "space")#turtle.update()
#wn.ontimer(advance_state_machine, 2000)
#wn.ontimer(advance_state_machine, 1000)
#time.sleep(3.5)

wn.listen()
wn.mainloop()
