from turtle import Turtle, speed
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color( random.choice(COLORS) )
        stretch = random.randint(2 , 5)
        self.shapesize(stretch_len=stretch , stretch_wid=1)
        self.length = 20 * stretch
      