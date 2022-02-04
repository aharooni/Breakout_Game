from turtle import Screen
from ball import Ball
from paddle import Paddle
from block import Block
from scoreboard import ScoreBoard
import time

FONT= ('Arial', 24, 'normal')


window = Screen()
window.setup(height=750, width=500)
window.bgcolor('black')
window.tracer(0)
window.listen()

blocks = []

def create_blocks():
    for i in range(0, 5):
        for j in range (0, 4):
            blocks.append(Block(-200+i*100 ,300 - j*40 ))

ball= Ball()
paddle= Paddle()
score = ScoreBoard()

window.onkey(paddle.moveback, 'a')
window.onkey(paddle.moveforward, 'd')

while True:
    time.sleep(0.01)
    ball.move_ball(paddle, blocks, score)

    if len(blocks) == score.score:
        create_blocks()
    if ball.ycor()<=-365:
        break
    window.update()

score.goto(0, 0)
score.write('GAME OVER', font=FONT, align='CENTER')
    

window.mainloop()