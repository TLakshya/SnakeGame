from turtle import Turtle

position = [(0, 0), (-20, 0), (-40, 0)]
speed = 20
UP = 90
DN = 270
LF = 180
RH = 0


class Snake:
    def __init__(self):
        self.block = []
        self.create_snake()
        self.head = self.block[0]

    def create_snake(self):
        for p in position:
            self.add(p)

    def add( self ,pos):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(pos)
        self.block.append(tim)

    def move(self):
        for s in range(len(self.block) - 1, 0, -1):
            x = self.block[s - 1].xcor()
            y = self.block[s - 1].ycor()
            self.block[s].goto(x, y)
        self.head.forward(speed)
    def up(self):
        if self.head.heading() != DN:
            self.head.setheading(90)

    def dn(self):
        if self.head.heading() != UP:
            self.head.setheading(-90)

    def lf(self):
        if self.head.heading() != RH:
            self.head.setheading(180)

    def rh(self):
        if self.head.heading() != LF:
            self.head.setheading(0)

    def extend(self):
        self.add(self.block[-1].position())
