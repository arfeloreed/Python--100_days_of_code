import turtle as t
INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    """A blueprint for creating the snake in the game"""
    def __init__(self):
        """Initialize the attributes for the class Snake"""
        self.snakes = []
        self.initial_snake()
        self.head = self.snakes[0]

    def initial_snake(self):
        """create the first body of the snake"""
        for position in INITIAL_POSITIONS:
            self.create_snake(position)

    def create_snake(self, position):
        """Create the snake objects"""
        snake = t.Turtle("square")
        snake.penup()
        snake.setpos(position)
        self.snakes.append(snake)

    def reset_snake(self):
        """Resets the snake to its initial stage"""
        for snake_old in self.snakes:
            snake_old.setpos(1000, 1000)
        self.snakes.clear()
        self.initial_snake()
        self.head = self.snakes[0]

    def snake_move(self):
        """Makes the snake automatically moves"""
        for i in range(len(self.snakes)-1, 0, -1):
            move_to = self.snakes[i - 1].pos()
            self.snakes[i].setpos(move_to)
        self.head.forward(20)

    def grow_snake(self):
        """Everytime the snake eats a food, adds a new snake object"""
        add_snake = self.snakes[-1].pos()
        self.create_snake(add_snake)

    def up(self):
        """Makes the snake move in the upward direction"""
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        """Makes the snake move in the downward direction"""
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        """Makes the snake move on the left side of the screen"""
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        """Makes the snake move on the right side of the screen"""
        if self.head.heading() != LEFT:
            self.head.setheading(0)
