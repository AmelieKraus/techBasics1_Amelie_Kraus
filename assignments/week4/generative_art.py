from turtle import *
import random

# Setup
width = 600
height = 1000
setup(width, height)
tracer(0, 0)
bgcolor('white')
pensize(2)
colormode(255)  # defines colours from 0-255

shapes = ["square", "circle", "triangle_up", "triangle_down", "star", "square"]

# --- top row (in black) ---> changes y so everything is on one line/row
x_pos = -260
pencolor(0, 0, 0)  #black
for shape in shapes:
    penup()
    if shape == "square":
        goto(x_pos, 435);
        pendown()
        for _ in range(4): forward(70); right(90)
    elif shape == "circle":
        goto(x_pos + 35, 435 - 70);
        pendown();
        circle(35)
    elif shape == "triangle_up":
        goto(x_pos, 435 - 70);
        pendown()
        for _ in range(3): forward(70); left(120)
    elif shape == "triangle_down":
        goto(x_pos, 435);
        pendown()
        for _ in range(3): forward(70); right(120)
    elif shape == "star":
        goto(x_pos + 35, 435 - 35);
        pendown()
        for _ in range(10): forward(35); backward(35); right(36)
    x_pos += 95 #x stays for everything

# --- middle part (colour gradient & hourglass shape) ---
for _ in range(70):
    y = random.randint(-300, 300)
    max_x = int(10 + (abs(y) / 300) * 210)
    x = random.randint(-max_x, max_x)
    size = random.randint(30, 60)
    choice = random.choice(["sq", "circ", "tri", "star"])

    # colour logic part: (had to look this one up)
    # Wir berechnen einen Faktor von 0 (oben) bis 1 (unten)
    # y=300 -> faktor=0 | y=-300 -> faktor=1
    faktor = (300 - y) / 600

    # mixing black (0,0,0) to a random colour
    r = int(random.randint(100, 255) * faktor)
    g = int(random.randint(0, 150) * faktor)
    b = int(random.randint(150, 255) * faktor)
    pencolor(r, g, b)

    penup()
    goto(x, y)
    pendown()

    if choice == "sq":
        for _ in range(4): forward(size); right(90)
    elif choice == "circ":
        circle(size // 2)
    elif choice == "tri":
        w = random.choice([120, -120])
        for _ in range(3): forward(size); left(w)
    elif choice == "star":
        for _ in range(8): forward(size // 2); backward(size // 2); right(45)

# --- bottom row (with colours) ---
x_pos = -260
for shape in shapes:
    # every shape gets its own colour
    pencolor(random.randint(100, 255), random.randint(0, 200), random.randint(100, 255))

    penup()
    y_br = -365  # y position (Y_bottom-row)
    if shape == "square":
        goto(x_pos, y_br);
        pendown()
        for _ in range(4): forward(70); right(90)
    elif shape == "circle":
        goto(x_pos + 35, y_br - 70);
        pendown();
        circle(35)
    elif shape == "triangle_up":
        goto(x_pos, y_br - 70);
        pendown()
        for _ in range(3): forward(70); left(120)
    elif shape == "triangle_down":
        goto(x_pos, y_br);
        pendown()
        for _ in range(3): forward(70); right(120)
    elif shape == "star":
        goto(x_pos + 35, y_br - 35);
        pendown()
        for _ in range(10): forward(35); backward(35); right(36)
    x_pos += 95

update()
exitonclick()