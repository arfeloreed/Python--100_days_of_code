import turtle as t
import snake as s

my_screen = t.Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("green")
my_screen.title("Snake Game")
my_screen.tracer(0)
# making 3 turtle objects align onto each other
kazuha = s.Snake()
# making the user controls the snake direction of movements
my_screen.listen()
my_screen.onkey(fun=kazuha.up, key="Up")
my_screen.onkey(fun=kazuha.down, key="Down")
my_screen.onkey(fun=kazuha.left, key="Left")
my_screen.onkey(fun=kazuha.right, key="Right")
# making the turtle objects move
kazuha.snake_move()

my_screen.exitonclick()
