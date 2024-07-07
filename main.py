from turtle import *
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time
s=Screen()
s.tracer(0)
s.setup(width=800,height=600)
s.bgcolor("black")
s.title("pong")
l_paddle=Paddle((-350,0))
r_paddle=Paddle((350,0))
ball=Ball()
score_board=Scoreboard()
s.listen()
s.onkey(r_paddle.go_up,"Up")
s.onkey(r_paddle.go_down,"Down")
s.onkey(l_paddle.go_up,"w")
s.onkey(l_paddle.go_down,"s")
game_is_on=True
while game_is_on:
    time.sleep(0.1)
    s.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()>320:
        ball.bounce_x()
    if ball.xcor()>380:
        ball.reset_position()
        score_board.l_point()
    if ball.xcor()<-380:
        ball.reset_position()
        score_board.r_point()
s.exitonclick()
