from random import random, randrange
from turtle import Turtle, Screen


def change_color():
    """A simple attempt to randomize the turtle's output color"""
    r = random()
    g = random()
    b = random()

    angela.color(r, g, b)


def is_in_screen(screen_size, turtle_position):
    """A simple function to describe whether the turtle is still on my window"""
    left_bound = -(screen_size.window_width() / 2)
    right_bound = screen_size.window_width() / 2
    top_bound = screen_size.window_height() / 2
    bottom_bound = -(screen_size.window_height() / 2)

    turtle_x = turtle_position.xcor()
    turtle_y = turtle_position.ycor()

    still_in = True
    if turtle_x > right_bound or turtle_x < left_bound:
        still_in = False
    if turtle_y > top_bound or turtle_y < bottom_bound:
        still_in = False
    return still_in


my_screen = Screen()
angela = Turtle()
angela.pensize(8)
angela.speed(6)
while is_in_screen(my_screen, angela):
    angela_move = randrange(0, 2)
    if angela_move == 0:
        angela.right(90)
    else:
        angela.left(90)
    change_color()
    angela.forward(30)

my_screen.exitonclick()
