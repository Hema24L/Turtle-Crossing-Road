from turtle import Turtle

MOVE = 30
FINISH = 260
STARTING_POS = (0, -260)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.shape('turtle')
        self.shapesize(2,2)
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POS)
    
    def up(self):
        self.forward(MOVE)
    
    def goto_start(self):
        self.goto(STARTING_POS)
    
    def at_finish(self):
        if self.ycor() > FINISH:
            return True
        else:
            return False
