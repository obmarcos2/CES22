import turtle

scr = turtle.Screen()
scr.bgcolor("lightgreen")
tur = turtle.Turtle()
tur.color("purple")

for i in range(6):
    tur.penup()
    tur.setposition(-10 * (i + 1), -10 * (i + 1))
    if i != 5:
        tur.pendown()
    for j in range(4):
        tur.fd(20 * (i + 1))
        tur.lt(90)

scr.mainloop()
