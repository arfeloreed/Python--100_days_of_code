import time
from turtle import Screen
import snake as s
import food as f
import score
WIDTH, HEIGHT = 600, 600

my_screen = Screen()
my_screen.setup(width=WIDTH, height=HEIGHT)
my_screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT)
my_screen.bgcolor("green")
my_screen.title("Snaky Game")
my_screen.tracer(0)

# create the snake object
snaky = s.Snake()
# control the direction the snake moves
my_screen.listen()
my_screen.onkey(fun=snaky.up, key="Up")
my_screen.onkey(fun=snaky.down, key="Down")
my_screen.onkey(fun=snaky.left, key="Left")
my_screen.onkey(fun=snaky.right, key="Right")

# make the food object
food = f.Food()
# create the score object
scoreboard = score.ScoreBoard()

# make the snake move
game_active = True
while game_active:
    time.sleep(0.1)
    my_screen.update()
    snaky.snake_move()

    # detect collision with food, count score and grow snake
    if snaky.head.distance(food) < 15:
        food.refresh_food()
        scoreboard.count_score()
        snaky.grow_snake()

    # game over sequences, displays Game Over
    # detect collision with wall
    if snaky.head.xcor() > 290 or snaky.head.xcor() < -290 or snaky.head.ycor() > 290 or snaky.head.ycor() < -290:
        game_active = False
        scoreboard.game_over()
    # detect collision with tail
    for snake in snaky.snakes[2:]:
        if snaky.head.distance(snake) < 10:
            game_active = False
            scoreboard.game_over()

my_screen.exitonclick()
