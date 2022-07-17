import turtle
from turtle import Turtle
import random

from constants import SCREEN_WIDTH, SCREEN_HEIGHT

turtle.colormode(255)


class Car(Turtle):
    def __init__(self, position):
        super().__init__()
        self.set_color()
        self.shape('square')
        self.shapesize(stretch_len=2)
        self.penup()
        self.setheading(180)
        self.setposition(position)
        self.speed('fastest')
        # self.set_car_position()

    def set_color(self):
        r = random.randint(0, 250)
        g = random.randint(0, 250)
        b = random.randint(0, 250)

        self.color((r, g, b))

    def set_car_position(self):
        # car_x = SCREEN_WIDTH / 2
        # y_edge = (SCREEN_HEIGHT / 2) - 70
        # car_y = random.randint(-y_edge, y_edge)

        car_x = 300
        car_y = random.randint(-280, 280)
        self.setposition(car_x, car_y)

    def move(self):
        """moves the car from the right to the left"""
        self.forward(10)
