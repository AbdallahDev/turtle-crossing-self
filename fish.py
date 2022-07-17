from turtle import Turtle

from constants import SCREEN_HEIGHT


class Fish(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape('turtle')
        self.setposition(x=0, y=-((SCREEN_HEIGHT / 2) - 20))

    def move(self):
        """move the fish forward"""
        if self.ycor() < (SCREEN_HEIGHT / 2) - 20:
            self.forward(10)
