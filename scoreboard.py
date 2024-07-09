from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.write(f"scores: {self.score}", align="center", font=("arial", 24, "normal"))
        self.hideturtle()
        self.update()


    def update(self):
        self.clear()
        self.score += 1
        self.write(f"scores: {self.score}", align="center", font=("courier", 24, "normal"))

    def gameover(self):
        self.goto(0, 0)
        self.write("The game is over", align="center", font=("courier", 24, "normal"))
