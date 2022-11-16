import time
import turtle as t
import snake as s
import food as f
import scoreboard as sb

my_screen = t.Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("green")
my_screen.title("Snake Game")
my_screen.tracer(0)
# making 3 turtle objects align onto each other
kazuha = s.Snake()
# make food for the snake that appears randomly within the screen
food = f.Food()
# making the user controls the snake direction of movements
my_screen.listen()
my_screen.onkey(fun=kazuha.up, key="Up")
my_screen.onkey(fun=kazuha.down, key="Down")
my_screen.onkey(fun=kazuha.left, key="Left")
my_screen.onkey(fun=kazuha.right, key="Right")
# making the turtle objects move
score = sb.Scoreboard()
game_active = True
while game_active:
    my_screen.update()
    time.sleep(0.1)
    score.clear()
    score.display_score()
    kazuha.snake_move()
    # detect collision between snake and food
    if kazuha.head.distance(food) < 17:
        food.refresh()
        # checks the current score for the user
        score.score += 1
        kazuha.grow_snaky()
    # detect collision with wall
    if kazuha.head.xcor() > 290 or kazuha.head.xcor() < -290 or kazuha.head.ycor() > 290 or kazuha.head.ycor() < -290:
        game_active = False
        score.is_game_over()
#     detect collision with tail
    for snake in kazuha.snakes[2:]:
        if kazuha.head.distance(snake) < 10:
            game_active = False
            score.is_game_over()

my_screen.exitonclick()
