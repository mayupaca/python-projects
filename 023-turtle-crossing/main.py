import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
car_generation_timer = time.time()
while game_is_on:
    time.sleep(0.1)
    # 0.1秒でスクリーンがアップデートされる
    screen.update()
    # スクリーンがアップデートされるたびに車が作られる
    car_manager.create_car()
    car_manager.move_cars()

    # The turtle hits the top edge of the screen
    if player.ycor() > 280:
        player.reset_position()
        car_manager.speed_up()
        scoreboard.level_up()

    # Check collision with player
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
