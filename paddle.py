from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.penup()
        #self.speed("fastest")
        self.goto(pos)
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color("white")

    def up(self):
        y = self.ycor() + 20
        self.goto(x=self.xcor(),y=y)

    def down(self):
        y = self.ycor() - 20
        self.goto(x=self.xcor(),y=y)