import time
import turtle
from turtle import Screen
from random import randint

from car import Car
from fish import Fish
from level import Level
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

difficulty_level = 1
end_game = False
cars_speed = 0.5

screen = Screen()


def game():
    fish = Fish()

    cars = []

    screen.onkey(fun=fish.move, key='Up')

    def generate_cars(car_xcor_par=300):
        new_car = Car(car_xcor=car_xcor_par, moving_distance=cars_speed)
        cars.append(new_car)

    def generate_first_bulk():
        for _ in range(30):
            car_xcor = randint(-300, 300)
            generate_cars(car_xcor)

    generate_first_bulk()

    while True:
        for car in cars:
            car.move()
            if car.distance(fish) < 25:
                return True

        appearance_x_range = randint(270, 280)
        if cars[-1].xcor() < appearance_x_range:
            generate_cars()

        if fish.ycor() > 260:
            level.increase_level()
            break

        screen.update()

    return False


while not end_game:
    turtle.clearscreen()

    screen = Screen()
    screen.colormode(255)
    screen.tracer(0)
    screen.listen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, startx=1)

    level = Level(level=difficulty_level)
    difficulty_level += 1

    end_game = game()

    cars_speed += 0.5

screen.exitonclick()
