from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('blue')
        self.shape('square')
        self.speed('fastest')
        self.turtlesize(stretch_wid=1, 
                        stretch_len=5)
        self.goto(0,-340)

    def moveforward(self):
        if self.xcor()<200:
            self.forward(20)

    def moveback(self):
        if self.xcor()>-200:
            self.backward(20)
