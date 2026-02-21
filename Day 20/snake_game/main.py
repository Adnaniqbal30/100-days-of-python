from turtle import Turtle,Screen
import time
from snake import Snake
screen=Screen()
screen.tracer(0)
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
snake=Snake()

game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)





















screen.exitonclick()