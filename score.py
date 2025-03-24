from turtle import Turtle

class Score(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.display_score()

    
    def display_score(self):
        self.write( arg= f"Score: {self.score}", move=False, align="center", font=('Arial', 24, 'normal'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.display_score()
    
    def game_over(self):
        self.goto(0,0)
        self.write( arg= "Game Over.", move=False, align="center", font=('Arial', 24, 'normal'))
    