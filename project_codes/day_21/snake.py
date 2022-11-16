import turtle as t
INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Represents the creation of a snake"""
    def __init__(self):
        """Initialize the attributes for the snake"""
        self.snakes = []
        self.create_snaky()
        self.head = self.snakes[0]

    def create_snaky(self):
        """Create 3 turtle objects."""
        for position in INITIAL_POSITIONS:
            self.snaky_blueprint(position)

    def snaky_blueprint(self, position):
        """Blueprint for creating snaky"""
        snaky = t.Turtle(shape="square")
        snaky.penup()
        snaky.setpos(position)
        self.snakes.append(snaky)

    def grow_snaky(self):
        """Angela grows everytime it collides with a food"""
        self.snaky_blueprint(self.snakes[-1].pos())

    def snake_move(self):
        """Makes the snake move automatically"""
        for i in range(len(self.snakes) - 1, 0, -1):
            move_to = self.snakes[i - 1].pos()
            self.snakes[i].setpos(move_to)
        self.head.forward(20)

    def up(self):
        """turns the snake in to upward position"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """turns the snake in to downward position"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """turns the snake into left position of the screen"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """turns the snake into right position of the screen"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
