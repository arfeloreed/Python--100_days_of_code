import time
from turtle import Screen
from paddle import Paddle
import ball as b
import score as s
WIDTH, HEIGHT = 800, 600

my_screen = Screen()
my_screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT)
my_screen.setup(width=WIDTH, height=HEIGHT+4)
my_screen.bgcolor("black")
my_screen.tracer(0)

# create paddles
r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
# control the paddle
my_screen.listen()
my_screen.onkey(fun=r_paddle.up, key="Up")
my_screen.onkey(fun=r_paddle.down, key="Down")
my_screen.onkey(fun=l_paddle.up, key="w")
my_screen.onkey(fun=l_paddle.down, key="s")

# create the ball object
ball = b.Ball()

# create scoreboard
r_score = s.Scoreboard((30, 250))
l_score = s.Scoreboard((-30, 250))

game_active = True
while game_active:
    time.sleep(ball.speed)
    ball.ball_move()
    my_screen.update()

    # the ball bounces when it hits the paddles
    if (ball.distance(r_paddle) < 80 and ball.xcor() == 360) or (ball.distance(l_paddle) < 80 and ball.xcor() == -360):
        ball.paddle_bounce()
    # if the ball hits the top and bottom wall
    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.y_wall_bounce()
    # if the ball hits the side walls
    if ball.xcor() > 390:
        ball.over_x_wall()
        l_score.add_score()
    elif ball.xcor() < -390:
        ball.over_x_wall()
        r_score.add_score()

my_screen.exitonclick()
