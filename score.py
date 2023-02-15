from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.r_scoring = 0
        self.l_scoring = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update()


    def update(self):
        self.goto(200, 150)
        self.write(self.r_scoring, align=ALIGNMENT, font=FONT)
        self.goto(-200, 150)
        self.write(self.l_scoring, align=ALIGNMENT, font=FONT)

    def if_r(self):
        self.r_scoring += 1
        self.clear()
        self.update()
    def if_l(self):
        self.l_scoring += 1
        self.clear()
        self.update()


