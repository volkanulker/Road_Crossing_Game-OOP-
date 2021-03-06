import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from level_sign import LevelSign

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


# Create objects
player = Player()
car_manager = CarManager()
level_sign = LevelSign()
car_manager.create_cars(5)


# Moving keys
screen.onkeypress(fun= player.move_up , key='Up')
screen.onkeypress(fun= player.move_down , key='Down')
screen.onkeypress(fun= player.move_right , key='Right')
screen.onkeypress(fun= player.move_left , key='Left')


game_is_on = True
# Game loop
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()
    car_manager.refresh_cars()

    # turtle crossing the lane
    if player.ycor() > 250:
        player.refresh_position()
        car_manager.increase_car_speed()
        level_sign.refresh_score()
        # Add 2 cars
        if car_manager.number_of_cars < 12:
            car_manager.create_cars(2)

    # If there is a collision finish the game
    if car_manager.is_there_collision(player):
        time.sleep(2)
        screen.reset()
        level_sign.game_over()
        game_is_on = False

screen.exitonclick()