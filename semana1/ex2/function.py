import turtle


def draw_poly(t, n, sz):
    angle = 360/n
    for i in range(n):
        t.forward(sz)
        t.left(angle)
    turtle.mainloop()
