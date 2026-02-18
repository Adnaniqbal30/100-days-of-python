import turtle
from turtle import Turtle,Screen

my_turtle=Turtle()
turtle.listen()

def move_forward():
    my_turtle.forward(10)

def move_backward():
    my_turtle.backward(10)

def move_counter_clock():
    my_turtle.left(10)

def move_clock():
    my_turtle.right(10)
def reset():
    my_turtle.home()
    my_turtle.clear()


turtle.onkey(key="w", fun=move_forward)
turtle.onkey(key="s", fun=move_backward)
turtle.onkey(key="a", fun=move_counter_clock)
turtle.onkey(key="d", fun=move_clock)
turtle.onkey(key="c", fun=reset)








screen=Screen()
screen.exitonclick()