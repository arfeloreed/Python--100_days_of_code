import turtle as t


class Paddle(t.Turtle):
    """Blueprint for creating paddle objects for pong game"""
    def __init__(self, position):
        """Initialize the attributes for the class Paddle"""
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        """Creates the additional needed info for the paddle object"""
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setpos(position)

    def up(self):
        """Simply move the paddle object upwards"""
        y_cor = self.ycor() + 20
        self.setpos(self.xcor(), y_cor)

    def down(self):
        """Simply move the paddle object upwards"""
        y_cor = self.ycor() - 20
        self.setpos(self.xcor(), y_cor)
