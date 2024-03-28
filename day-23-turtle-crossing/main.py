import time
from tkinter import PhotoImage
from turtle import Screen, Shape
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
car_img = "car.gif"
tyrone_img = "tyrone.gif"


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car = PhotoImage(file=car_img).subsample(10, 10)
tyrone = PhotoImage(file=tyrone_img).subsample(3, 3)
screen.addshape("car", Shape("image", car))
screen.addshape("tyrone", Shape("image", tyrone))

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.move_cars()
    screen.update()

    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            player.reset_position()

    if player.is_at_finish_line():
        player.reset_position()
        car_manager.level_up()
        scoreboard.increase_score()




screen.exitonclick()
