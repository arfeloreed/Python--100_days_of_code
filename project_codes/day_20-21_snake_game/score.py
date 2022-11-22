import turtle as t


class ScoreBoard(t.Turtle):
    """A subclass of the class Turtle"""
    def __init__(self):
        """Initialize the attributes for the subclass ScoreBoard"""
        super().__init__()
        self.penup()
        self.setpos(-270, 260)
        self.score = 0
        self.display_score()
        self.hideturtle()

    def display_score(self):
        """Display the current score in the screen"""
        self.clear()
        self.write(arg=f"Score: {self.score}", font=("Arial", 20, "underline"))

    def count_score(self):
        """Adds 1 to the current score everytime the snake eats a food"""
        self.score += 1
        self.display_score()

    def game_over(self):
        """Displays Game Over in the screen"""
        self.setpos(0, 0)
        self.write(arg="Game Over", align="center", font=("Arial", 26, "underline"))
