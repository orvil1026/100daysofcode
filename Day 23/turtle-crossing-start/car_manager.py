from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_COORDINATES = [0, 50, 100, 150, 200, -50, -100, -150, -200]


class CarManager:

    def __init__(self):
        self.cars = []
        self.car_speed = MOVE_INCREMENT

    def create_car(self):
        time.sleep(0.1)
        new_car = Turtle()
        new_car.penup()
        new_car.shape('square')
        new_car.color(random.choice(COLORS))
        new_car.turtlesize(stretch_len=2)
        new_car.goto(280, random.choice(Y_COORDINATES))
        new_car.setheading(180)
        self.cars.append(new_car)

    def move(self):

        for cars in self.cars:
            cars.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += 10
