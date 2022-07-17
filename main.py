from turtle import Screen
import time
from random import randint, choice

from car import Car
from fish import Fish
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

screen = Screen()
screen.tracer(0)
screen.listen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, startx=1)

fish = Fish()
cars = []

ranges = [(-280, -210), (-210, -140), (-140, -70), (-70, 0), (0, 70), (70, 140), (140, 210), (210, 280)]

screen.onkey(fun=fish.move, key='Up')

while True:
    y_range = choice(ranges)
    y = randint(y_range[0], y_range[1])
    new_car = Car((280, y))
    for _ in range(10000000):
        pass
    cars.append(new_car)

    for car in cars:
        car.move()

    screen.update()
    time.sleep(0.5)

# screen.exitonclick()
