import turtle as t


class Scoreboard(t.Turtle):
    """A subclass from Turtle"""
    def __init__(self, position):
        """Initialize the attributes for the subclass Scoreboard"""
        super().__init__()
        self.penup()
        self.color("white")
        self.setpos(position)
        self.score = 0
        self.display_score(self.score)
        self.hideturtle()

    def display_score(self, score):
        """Displays the current score"""
        self.write(score, font=("Arial", 25, "normal"))

    def score_plus(self):
        """Adds score by 1 everytime the other user can't return the ball"""
        self.score += 1
        self.clear()
        self.display_score(self.score)
