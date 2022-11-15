import random as r
import turtle as t

my_screen = t.Screen()
my_screen.setup(width=600, height=500)
is_race_on = False
user_bet = my_screen.textinput(title="Make a bet", prompt="Enter a color for a turtle you want to place your bet: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
x_cor = -280
y_cor = -125
all_kazuhas = []

for i in range(6):
    kazuha = t.Turtle(shape="turtle")
    kazuha.color(colors[i])
    kazuha.penup()
    kazuha.setpos(x_cor, y_cor)
    y_cor += 50
    all_kazuhas.append(kazuha)

if user_bet:
    is_race_on = True

while is_race_on:
    for kazuha in all_kazuhas:
        distance_run = r.randint(1, 10)
        kazuha.forward(distance_run)
        if kazuha.xcor() > 275:
            is_race_on = False
            if user_bet == kazuha.pencolor():
                print(f"You've won. The {kazuha.pencolor()} turtle is the winner.")
            else:
                print(f"You've lost. The {kazuha.pencolor()} turtle is the winner.")

my_screen.exitonclick()
