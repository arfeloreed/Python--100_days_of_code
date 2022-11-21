import turtle as t
FONT = ("Courier", 24, "normal")


class Scoreboard(t.Turtle):
    """A subclass of Turtle class"""
    def __init__(self):
        """Initialize the attributes for Scoreboard"""
        super().__init__()
        self.penup()
        self.level = 1
        self.setpos(-280, 250)
        self.hideturtle()

    def display_level(self):
        """Displays the current level of Gabby"""
        self.write(arg=f"Level: {self.level}", font=FONT)

    def increase_level(self):
        """Increases Gabby's current level everytime she reaches the finishline"""
        self.level += 1

    def game_over(self):
        """Displays a game over when Gabby collides with a car"""
        self.setpos(0, 0)
        self.write(arg="Game Over", align="center", font=FONT)
