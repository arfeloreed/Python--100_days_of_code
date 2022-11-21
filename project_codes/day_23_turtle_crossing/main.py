import time
import turtle as t
import gabby as g
import cars as c
import score as s
WIDTH, HEIGHT = 600, 600

# set screen
my_screen = t.Screen()
my_screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT)
my_screen.setup(width=WIDTH+2, height=HEIGHT+2)
my_screen.title("Gabby the turtle")
my_screen.tracer(0)
# create gabby
gabby = g.Gabby((0, -280))
car = c.Car()
scoreboard = s.Scoreboard()
# making gabby move
my_screen.listen()
my_screen.onkey(fun=gabby.up, key="Up")

game_active = True
while game_active:
    my_screen.update()
    time.sleep(0.1)
    scoreboard.display_level()
    # generate cars
    car.create_car()
    car.auto_move()
    # if gabby reaches finish line
    if gabby.ycor() == 280:
        gabby.setpos(0, -280)
        car.increase_difficulty()
        scoreboard.clear()
        scoreboard.increase_level()

    # checks if gabby collides with a car
    for i in range(len(car.cars)):
        if gabby.distance(car.cars[i]) < 25:
            game_active = False
            scoreboard.game_over()

my_screen.exitonclick()
