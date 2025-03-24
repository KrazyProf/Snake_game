from turtle import Screen
from snake import Snake 
from food import Food
from score import Score
import time


screen = Screen()
screen.setup(width=600 , height=600)
screen.bgcolor('black')
screen.tracer(0) # --> turns off the turtle animation

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(key='Up' , fun=snake.move_up)
screen.onkey(key='Down' , fun=snake.move_down)
screen.onkey(key='Left' , fun=snake.turn_left)
screen.onkey(key='Right' , fun=snake.turn_right)
    

is_over = False
while not is_over:
    screen.update()
    time.sleep(0.1)

    snake.move()
    
    # Detecting Collision with wall
    if snake.head.xcor() > 270 or snake.head.xcor() < -270 or snake.head.ycor() > 270 or snake.head.ycor() < -270:
        score.game_over()
        break

    if snake.head.distance(snake.snake_body[-1]) < 14:
        print('crash')
    # Detecting collision
    if snake.head.distance(food) < 14:
        
        # getting food to respawn
        food.refresh()  
        # updating the score
        score.update_score()
        # adding body parts
        snake.add_body_part()
        

    for segment in snake.snake_body:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score.game_over()
            is_over = True
            break

screen.exitonclick()