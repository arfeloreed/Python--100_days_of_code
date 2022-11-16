import turtle as t


class Scoreboard(t.Turtle):
    """A subclass with Turtle as the parent class"""
    def __init__(self):
        """Initialize the attributes for the subclass Scoreboard"""
        super().__init__()
        self.penup()
        self.score = 0
        self.setpos(0, 260)
        self.hideturtle()
        self.display_score()

    def is_game_over(self):
        """Displays a game over message in the screen for the user"""
        self.setpos(0, 0)
        self.write(arg="GAME OVER.", align="center", font=("Arial", 24, "normal"))

    def display_score(self):
        """Display the current score everytime the snake collides with the food"""
        self.write(arg=f"Score: {self.score}", align="center", font=("Arial", 12, "normal"))
