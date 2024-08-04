import time
from turtle import Screen, Turtle
from Paddle import Paddle
from ball import Ball
from scoreBoard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width = 1000, height = 600)
screen.title("Pong")

r_paddle = Paddle((460,0))
l_paddle = Paddle((-460,0))
ball = Ball()
scoreBoard = Scoreboard()







screen.listen()

screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.03)
    ball.move()

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.y_bounce()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 440 or ball.distance(l_paddle) < 50 and ball.xcor() < -440:
        ball.x_bounce()
        ball.x_move *= 1.1
        ball.y_move *= 1.1

    if ball.xcor() > 480:
        ball.reset_position()
        scoreBoard.l_point()

    if ball.xcor() < -480:
        ball.reset_position()
        scoreBoard.r_point()



    if r_paddle.ycor() > 250:
        r_paddle.setposition(r_paddle.xcor(), 250)
    elif r_paddle.ycor() < -250:
        r_paddle.setposition(r_paddle.xcor(), -250)

    if l_paddle.ycor() > 250:
        l_paddle.setposition(l_paddle.xcor(), 250)
    elif l_paddle.ycor() < -250:
        l_paddle.setposition(l_paddle.xcor(), -250)

screen.exitonclick()