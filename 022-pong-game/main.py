from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# create a new screen for the game
screen = Screen()
screen.setup(800, 600)
# set the background color to black
screen.bgcolor("black")
# change the title
screen.title("Pong")
# .tracerでパドルのアニメーションを止める。
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# listen for keyboad input
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    # .tracerで一時停止していたアニメーションの処理を実行して表示させる
    screen.update()
    # スクリーンがリフレッシュされるたびにballメソッドが呼び出されるからボールが移動する
    ball.move()

    # Detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if ball goes out of bounds(R)
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect if ball goes out of bounds(L)
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
