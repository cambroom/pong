from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.ymove = 20
        self.xmove = 20
    def move(self):
        ballx = self.xcor() + self.xmove
        bally = self.ycor() + self.ymove
        self.goto(ballx, bally)
    def ymoves(self):
        self.ymove *= -1
    def xmoves(self):
        self.xmove *= -1
    def reset(self):
        self.home()
        self.xmoves()