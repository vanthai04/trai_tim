import turtle

t = turtle.Turtle()
t.speed(5)
t.color("red")
t.begin_fill()

t.left(140)
t.forward(180)
t.circle(-90, 200)
t.left(120)
t.circle(-90, 200)
t.forward(180)

t.end_fill()

t.penup()
t.goto(0, -40)  
t.color("white") # chữ màu trắng cho nổi trên nền đỏ
t.write(
    "Yêu vợ Hương iuuuu nhiềuuu",
    align="center",
    font=("Arial", 16, "bold")
)
turtle.done()