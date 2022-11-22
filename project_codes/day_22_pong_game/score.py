import turtle as t


class Scoreboard(t.Turtle):
    """A subclass of Turtle class"""
    def __init__(self, position):
        """Initialize the attributes for the subclass Scoreboard"""
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        self.setpos(position)
        self.display_score()
        self.hideturtle()

    def display_score(self):
        """Displays the current score in the screen"""
        self.clear()
        self.write(arg=f"{self.score}", font=("Arial", 24, "normal"))

    def add_score(self):
        """Adds 1 to the current score everytime the player scores"""
        self.score += 1
        self.display_score()
