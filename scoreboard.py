from turtle import Turtle
FONT = ('arial', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.hideturtle()
        self.score = 0
        self.update_score()


    def update_score(self):
        self.goto(-225, 325)
        self.clear()
        self.write(f'Score: {self.score}', font= FONT)

    def increment_score(self):
        self.score += 1
        self.update_score()