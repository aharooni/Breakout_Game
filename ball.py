from turtle import Turtle
import random
SPEED = 5
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(1)
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.goto(0, -300)
        self.setheading(random.randint(45,135))
        self.multiplier = 0

    def move_ball(self, paddle, blocks, score):
        self.forward(SPEED + self.multiplier)

        if self.xcor()>=240 \
                or self.xcor()<=-240:
            self.setheading(180-self.heading())

        if self.ycor()>=365:
            self.setheading(360-self.heading())

        if (paddle.xcor()+50)>=self.xcor()>=(paddle.xcor()-50)\
                and (self.ycor()-paddle.ycor())<=20:

            angle = (paddle.xcor()-self.xcor())/50 * 60
            heading = 360-self.heading()+angle

            if 0<heading<30:
                self.setheading(30)
            elif 180>heading>150:
                self.setheading(150)
            else:
                self.setheading(360 - self.heading()+angle)

        for block in blocks:
            if (block.xcor() + 50) >= self.xcor() >= (block.xcor() - 50) \
                    and abs(self.ycor() - block.ycor()) <= 20:
                self.setheading(360 - self.heading())
                block.hideturtle()
                if score.score%10==0:
                    self.multiplier = self.multiplier+1
                block.goto(1000,1000)
                score.increment_score()


