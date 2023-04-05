from turtle import Screen
import time
from snake import Snake
import food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake: Python Edition")
screen.tracer(0)
game_is_on = True

snake = Snake()
food = food.Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.update()

while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect food
    if snake.head.distance(food) < 15:
        print("om nom nom")
        food.refresh()
        snake.add_segment()
        score.clear()
        score.add_score()
    # Detect wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280:
        game_is_on = False
        score.game_over()
    elif snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()
    # Detect own body
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_is_on = False
            score.game_over()











screen.exitonclick()
