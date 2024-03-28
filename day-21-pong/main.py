from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(goto_x=350, goto_y=0)
left_paddle = Paddle(goto_x=-350, goto_y=0)
ball = Ball()
left_scoreboard = Scoreboard(-100, 200)
right_scoreboard = Scoreboard(100, 200)

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect when right paddle misses
    if ball.xcor() > 380:
        left_scoreboard.increase_score()
        ball.reset_position()

    # Detect when left paddle misses
    if ball.xcor() < -380:
        right_scoreboard.increase_score()
        ball.reset_position()

screen.exitonclick()
