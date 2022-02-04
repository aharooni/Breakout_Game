from turtle import Turtle
import random

COLOR = ['red', 'purple', 'green', 'pink', 'cyan', 'cyan']

class Block(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.color(random.choice(COLOR))
        self.shape('square')
        self.turtlesize(stretch_wid=1.5,
                        stretch_len=4.5)
        self.goto(x, y)