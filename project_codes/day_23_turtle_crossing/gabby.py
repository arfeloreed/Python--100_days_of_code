import turtle as t


class Gabby(t.Turtle):
    """A subclass of Turtle class"""
    def __init__(self, position):
        """Initialize the attributes for Gabby"""
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.setpos(position)

    def up(self):
        """Moves Gabby in upward direction"""
        self.forward(10)
