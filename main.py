from turtle import Turtle, Screen
from food import Food
from scoreboard import Score
from snake import Snake
import time


screen = Screen()
screen.setup(600, 600)
screen.title("snake game")
screen.bgcolor("black")
screen.tracer(0.5)

snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.dn,"Down")
screen.onkey(snake.lf,"Left")
screen.onkey(snake.rh,"Right")

game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 50:
        food.refresh()
        snake.extend()
        score.update()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game = False
        score.gameover()
    for seg in snake.block:
        if snake.head.distance(seg) < 10 && snake.head.distance(seg) >1:
            game=False
            score.gameover()




screen.exitonclick()
