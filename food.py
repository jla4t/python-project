from turtle import Turtle
from random import randint as rand


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("yellow")
        self.speed(0)
        self.goto(rand(-275, 275), rand(-275, 275))

    def refresh(self):
        self.goto(rand(-275, 275), rand(-275, 275))