import turtle as t
import random

my_turtle=t.Turtle()
my_turtle.shape()
t.colormode(255)
my_turtle.speed(0)
def random_color():
    r=random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color=(r,g,b)
    return rand_color


def draw_spirograph(size_of_the_gap):
    for i in range(int(360/size_of_the_gap)):
        my_turtle.color(random_color())
        my_turtle.circle(100)
        my_turtle.setheading(my_turtle.heading()+size_of_the_gap)


draw_spirograph(5)







screen=t.Screen()
screen.exitonclick()