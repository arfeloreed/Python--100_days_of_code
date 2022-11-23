import turtle as t


class ScoreBoard(t.Turtle):
    """A subclass of the class Turtle"""
    def __init__(self):
        """Initialize the attributes for the subclass ScoreBoard"""
        super().__init__()
        self.penup()
        self.setpos(-270, 260)
        self.score = 0
        self.high_score = self.retrieve_high_score()
        self.display_score()
        self.hideturtle()

    def display_score(self):
        """Display the current score in the screen"""
        self.clear()
        self.write(arg=f"Score: {self.score}    High Score: {self.high_score}", font=("Arial", 20, "underline"))

    def count_score(self):
        """Adds 1 to the current score everytime the snake eats a food"""
        self.score += 1
        self.display_score()

    def reset_score(self):
        """Resets the current score to 0 and updates the high score"""
        if self.score > self.high_score:
            self.high_score = self.score
            self.set_high_score()
        self.score = 0
        self.display_score()

    def set_high_score(self):
        """Gets the high score and saves it to high_score.txt"""
        with open("high_score.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    def retrieve_high_score(self):
        """Retrieves the high score value from high_score.txt"""
        with open("high_score.txt") as file:
            content = int(file.read())
            return content
