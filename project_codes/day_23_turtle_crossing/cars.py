import random as r
import turtle as t
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car:
    """A blueprint for creating a car"""
    def __init__(self):
        """Initialize the attributes for class Car"""
        self.cars = []
        self.current_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Randomly generates y coordinates for position of car object"""
        chance = r.randint(1, 7)
        if chance == 1:
            car = t.Turtle()
            car.shape("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(r.choice(COLORS))
            x_cor = 300
            y_cor = r.randint(-250, 250)
            car.setpos(x_cor, y_cor)
            self.cars.append(car)

    def auto_move(self):
        """Automatically moves the turtle objects"""
        for car in self.cars:
            car.backward(self.current_speed)

    def increase_difficulty(self):
        """Increase the speed of the cars everytime gabby increase in level"""
        self.current_speed += MOVE_INCREMENT
