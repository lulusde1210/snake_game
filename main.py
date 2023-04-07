from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.add_score()
        snake.extend()

    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300 \
            or snake.head.ycor() >= 300 or snake.head.ycor() <= -300:
        is_game_on = False
        score_board.game_over()

    for i in range(2, len(snake.segments)):
        if snake.head.distance(snake.segments[i]) < 10:
            is_game_on = False
            score_board.game_over()

screen.exitonclick()
