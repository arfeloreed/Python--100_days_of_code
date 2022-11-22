import random as r
from turtle import Turtle


class Food(Turtle):
    """A subclass of class Turtle"""
    def __init__(self):
        """Initialize the attributes for the subclass Food"""
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh_food()

    def refresh_food(self):
        """Generates a random food in random position everytime the snake eats the current food"""
        x_cor = r.randint(-280, 280)
        y_cor = r.randint(-280, 280)
        self.setpos(x_cor, y_cor)
