import random
import colors
import turtle as t


def random_color():
    """randomize the output color for the turtle"""
    color = random.choice(colors.rgb_colors)
    color = kazuha.color(color)
    return color


def drawing_circles():
    """Draws randomize colored circles"""
    for i in range(10):
        kazuha.forward(50)
        kazuha.pendown()
        random_color()
        kazuha.begin_fill()
        kazuha.circle(10)
        kazuha.end_fill()
        kazuha.penup()


kazuha = t.Turtle()
my_screen = t.Screen()
t.colormode(255)
kazuha.speed(0)
kazuha.penup()
kazuha.hideturtle()
kazuha.setpos(-260, -230)
x_cor = kazuha.xcor()
y_cor = kazuha.ycor()

for i in range(10):
    drawing_circles()
    kazuha.setx(x_cor)
    y_cor += 50
    kazuha.sety(y_cor)

my_screen.exitonclick()
