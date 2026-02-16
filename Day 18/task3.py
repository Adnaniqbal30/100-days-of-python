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

for i in range(50):
    my_turtle.color(random_color())
    my_turtle.circle(100)









screen=t.Screen()
screen.exitonclick()