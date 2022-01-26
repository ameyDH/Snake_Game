from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game Amey")

screen.tracer(0)

snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect collision with wall
    if snake.segments[0].xcor()> 290 or snake.segments[0].xcor()< -290 or snake.segments[0].ycor()>290 or snake.segments[0].ycor()<-290 :
        score.game_over()
        game_is_on = False

    # Detect collision with tail
    for seg in snake.segments[1:]:

        # if snake.segments[0] == seg:
        #     pass
        
        if snake.segments[0].distance(seg) < 15:
            score.game_over()
            game_is_on = False

screen.exitonclick()
