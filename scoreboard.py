from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.inc_lvl = 1
        self.hideturtle()
        self.penup()
        self.goto(-250,270)
        self.update_scoreboard()

    
    def update_scoreboard(self):
        self.write(f"LEVEL:{self.inc_lvl}", font=('Arial', 16, 'normal'))
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align='center', font=('Arial', 16, 'normal'))

    
    def level_up(self):
        self.inc_lvl += 1
        self.clear()
        self.update_scoreboard()