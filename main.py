from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

scoreboard = Scoreboard()

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()
# ball.speed("slowest")
# ball.goto(380,280)



screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "z")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect when R paddle misses
    if ball.xcor() > 380:
        scoreboard.increase_l_score()
        ball.refresh()


    # Detect when L paddle misses
    if ball.xcor() < -380:
        scoreboard.increase_r_score()
        ball.refresh()











screen.exitonclick()