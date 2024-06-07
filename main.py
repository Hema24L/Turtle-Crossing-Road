from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor('white')
screen.title('Turtle Crossing')
screen.tracer(0)

player = Player()
cars = Cars()
score = Scoreboard()

screen.listen()
screen.onkey(player.up,'Up')

game_is = True
while game_is:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()
    
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is = False
            score.game_over()

    if player.at_finish():
        player.goto_start()
        cars.level_up()
        score.level_up()
    

screen.exitonclick()