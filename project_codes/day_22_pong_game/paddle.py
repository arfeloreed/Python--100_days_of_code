from turtle import Turtle


class Paddle(Turtle):
    """A subclass of the class Turtle"""
    def __init__(self, position):
        """Initialize the attributes for the subclass Paddle"""
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setpos(position)
        self.y_cor = self.ycor()

    def up(self):
        """Moves the paddle in an upward direction"""
        self.y_cor += 20
        self.setpos(self.xcor(), self.y_cor)

    def down(self):
        """Moves the paddle in a downward direction"""
        self.y_cor -= 20
        self.setpos(self.xcor(), self.y_cor)
