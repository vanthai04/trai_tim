import turtle

t = turtle.Turtle()
t.speed(5)
t.width(2)

# Hàm vẽ hình chữ nhật
def rectangle(w, h, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()

# Hàm vẽ hình tam giác
def triangle(size, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

# Thân nhà (đỏ)
t.penup()
t.goto(-100, -100)
t.pendown()
rectangle(200, 150, "orangered")

# Mái nhà (vàng)
t.penup()
t.goto(-120, 50)
t.pendown()
t.fillcolor("gold")
t.begin_fill()
t.goto(0, 160)
t.goto(120, 50)
t.goto(-120, 50)
t.end_fill()

# Cửa (trắng)
t.penup()
t.goto(-30, -100)
t.pendown()
rectangle(60, 90, "white")

# Tay nắm cửa
t.penup()
t.goto(20, -60)
t.dot(8, "black")

# Cửa sổ trái
t.penup()
t.goto(-85, -20)
t.pendown()
rectangle(50, 50, "blue")

# Cửa sổ phải
t.penup()
t.goto(35, -20)
t.pendown()
rectangle(50, 50, "blue")

# Ống khói
t.penup()
t.goto(50, 90)
t.pendown()
rectangle(20, 50, "blue")

t.hideturtle()
turtle.done()
