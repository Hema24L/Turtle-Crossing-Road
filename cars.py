from turtle import Turtle
import random

COLORS = ['red', 'blue', 'green', 'yellow','orange', 'purple']
START_DISTANCE = 5
MOVE = 10

class Cars():
    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE
        
    
    def create_car(self):
        control_cars = random.randint(1,6)
        if control_cars == 1 :
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid = 1, stretch_len = 3)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-200,200)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)


    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
    
    def level_up(self):
        self.car_speed += MOVE

        

