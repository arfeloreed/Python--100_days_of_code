import random
import turtle as t


def random_color():
    """Randomize the output color of the turtle"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    tup = (r, g, b)
    return tup


my_screen = t.Screen()
circle = t.Turtle()
t.colormode(255)
circle.speed(0)
circle.pensize(1)
while True:
    circle.left(5)
    circle.color(random_color())
    circle.circle(100)
    if circle.heading() == 0:
        break

my_screen.exitonclick()
