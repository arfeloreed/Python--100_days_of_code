import turtle as t


class Ball(t.Turtle):
    """Create a Ball class with Turtle class as the parent"""
    def __init__(self, pos):
        """Initialize the attributes for the class Ball"""
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.setpos(pos)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def ball_moving(self):
        """Automatically moves the ball"""
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.setpos(x_cor, y_cor)

    def ball_wall_bounce(self):
        """Change in ball movement if it hits the wall at the top"""
        self.y_move *= -1

    def ball_paddle_bounce(self):
        """Change in ball movement if it hits the paddle"""
        self.x_move *= -1
        self.ball_speed *= 0.9

    def ball_switch(self):
        """Switches the side where the ball should start bouncing"""
        self.setpos(0, 0)
        self.ball_speed = 0.1
        self.x_move *= -1
