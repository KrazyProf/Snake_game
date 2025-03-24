from turtle import Turtle

class Score(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.write( arg= f"Score: {self.score}", move=False, align="center", font=('Arial', 24, 'normal'))

        
    def update_score(self):
        self.score += 1
        self.clear()
        self.write( arg= f"Score: {self.score}", move=False, align="center", font=('Arial', 24, 'normal'))