import time
from turtle import Turtle , Screen
from paddle import paddle
from ball import Ball
from score_board import score
from quit_game import QuitGame

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800 , height=600)
screen.title('pong')
screen.tracer(0)


over = QuitGame()

r_paddle = paddle((350,0))
l_paddle = paddle((-350 ,0))
ball = Ball()
score_board = score()


def qui_game():
    global game_is_on
    game_is_on = False
    over.display_game_over()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up , "w")
screen.onkey(l_paddle.go_down,"s")
screen.onkey(qui_game, "Escape")




game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    # detect collision with r_paddle

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score_board.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score_board.r_point()



screen.exitonclick()

