from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
    # Creating Snake Body
        for i in range(3):
            new_snake = Turtle(shape='square')
            new_snake.penup()
            new_snake.color('white')
            new_snake.goto(-20 * i , 0)
            self.snake_body.append(new_snake)


    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def move(self):
        # moving the snake 
        for i in range(len(self.snake_body) - 1, 0 , -1):
            self.snake_body[i].goto(self.snake_body[i - 1].position())

        self.head.fd(MOVE_DISTANCE)
 