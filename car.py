import turtle
from turtle import Turtle
import random

turtle.colormode(255)


class Car(Turtle):
    def __init__(self, car_xcor, moving_distance):
        super().__init__()
        self.set_color()
        self.shape('square')
        self.shapesize(stretch_len=2)
        self.penup()
        self.setheading(180)
        self.speed('fastest')
        self.car_xcor = car_xcor
        self.set_car_position()
        self.moving_distance = moving_distance

    def set_color(self):
        r = random.randint(0, 250)
        g = random.randint(0, 250)
        b = random.randint(0, 250)

        self.color((r, g, b))

    def set_car_position(self):
        car_x = self.car_xcor
        car_y = random.randint(-230, 230)
        self.setposition(car_x, car_y)

    def move(self):
        """moves the car from the right to the left by a specific distance"""
        self.forward(self.moving_distance)
