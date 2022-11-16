import random as r
import turtle as t


class Food(t.Turtle):
    """A subclass for the Turtle class as parent."""
    def __init__(self):
        """Initialize the attributes for the subclass Food"""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed(0)
        self.refresh()

    def refresh(self):
        """Randomly generate food within the screen everytime the snake collides with the food."""
        random_x_cor = r.randint(-270, 270)
        random_y_cor = r.randint(-270, 270)
        self.setpos(random_x_cor, random_y_cor)
