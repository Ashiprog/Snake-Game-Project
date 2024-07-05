from turtle import Screen
from S_game import S_game
from scoreboard import Scoreboard
from food import Food
import time

my_screen = Screen()
my_screen.setup(600,600)
my_screen.bgcolor("black")
my_screen.title("The S game")
my_screen.tracer(0)
game_on = True

s_game = S_game()
food = Food()
scoreboard = Scoreboard()
my_screen.listen()
my_screen.onkey(s_game.up,"Up")
my_screen.onkey(s_game.down,"Down")
my_screen.onkey(s_game.left,"Left")
my_screen.onkey(s_game.right,"Right")

while game_on:
    my_screen.update()

    time.sleep(0.3)
    s_game.move_s()
#detect collision with food
    if s_game.head.distance(food) < 25:
        food.refresh()
        scoreboard.increase_score()



my_screen.exitonclick()
