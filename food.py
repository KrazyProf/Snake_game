from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("yellow")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed(0)
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-240, 280)
        rand_y = random.randint(-240, 280)
        self.goto(rand_x, rand_y)

