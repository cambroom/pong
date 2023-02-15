import random
from turtle import Turtle, Screen
from lines import Lines
from ball import Ball
from score import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_line = Lines((350,0))
l_line = Lines((-350,0))
ball = Ball()
score = Score()
screen.listen()
screen.onkey(r_line.up, "Up")
screen.onkey(r_line.down, "Down")
screen.onkey(l_line.up, "w")
screen.onkey(l_line.down, "s")
speed = 0.2
randheading = random.randint(180,360)
randerheading = random.randint(0,180)
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(speed)

    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.ymoves()
    if ball.distance(r_line) < 50 and ball.xcor() > 320 or ball.distance(l_line) < 50 and ball.xcor() < -320:
        ball.xmoves()
    if ball.xcor() > 390:
        ball.reset()
        score.if_l()
        speed *= .9
    if ball.xcor() < -390:
        ball.reset()
        score.if_r()
        speed *= .9
screen.exitonclick()
