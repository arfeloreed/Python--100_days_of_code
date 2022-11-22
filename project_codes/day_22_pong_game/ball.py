from turtle import Turtle


class Ball(Turtle):
    """A subclass of the Turtle class"""
    def __init__(self):
        """Initialize the attributes for the subclass Ball"""
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed = 0.1

    def ball_move(self):
        """Automatically moves the ball"""
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.setpos(x_cor, y_cor)

    def y_wall_bounce(self):
        """The ball bounces when it hits the top and bottom wall"""
        self.y_move *= -1

    def over_x_wall(self):
        """Resets the ball position into the center when it hits the side walls"""
        self.setpos(0, 0)
        self.speed = 0.1
        self.x_move *= -1

    def paddle_bounce(self):
        """The ball bounces when it hits the paddle and the speed increases"""
        self.speed *= 0.9
        self.x_move *= -1
