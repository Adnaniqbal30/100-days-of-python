import turtle as t
import random

my_turtle=t.Turtle()
my_turtle.shape()
t.colormode(255)

def random_color():
    r=random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color=(r,g,b)
    return rand_color

random_direction=[0,90,180,270]
my_turtle.speed(0)

for i in range(100):
    my_turtle.color(random_color())
    my_turtle.pensize(10)
    my_turtle.forward(30)
    my_turtle.setheading(random.choice(random_direction))










screen=t.Screen()
screen.exitonclick()