from turtle import Turtle


class Level(Turtle):
    def __init__(self, level):
        super().__init__()
        self.level = level
        self.hideturtle()
        self.penup()
        self.setposition(-290, 250)
        self.write_level()

    def write_level(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align='left', font=('Arial', 20, 'bold'))

    def increase_level(self):
        self.level += 1
        self.write_level()
