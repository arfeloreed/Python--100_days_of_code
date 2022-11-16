import time
import turtle as t
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Represents the creation of a snake"""
    def __init__(self):
        """Initialize the attributes for the snake"""
        self.x_cor = 0
        self.y_cor = 0
        self.my_screen = t.Screen()
        self.angelas = []

        for i in range(3):
            angela = t.Turtle(shape="square")
            angela.penup()
            angela.setpos(self.x_cor, self.y_cor)
            self.angelas.append(angela)
            self.x_cor += 20

        self.head = self.angelas[0]

    def snake_move(self):
        """Makes the snake move automatically"""
        game_active = True
        while game_active:
            self.my_screen.update()
            time.sleep(0.1)
            for i in range(len(self.angelas) - 1, 0, -1):
                move_to = self.angelas[i - 1].pos()
                self.angelas[i].setpos(move_to)
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
