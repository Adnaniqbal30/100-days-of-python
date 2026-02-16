from turtle import Turtle,Screen
import random

my_turtle=Turtle()
my_turtle.shape("turtle")
random_color=["#7FFF00","#4682B4","#F0E68C","#FF0000","#483D8B","#800080","#8A2BE2","#0000FF","#808000","#BC8F8F","#00FFFF"
              ,"#FFFF00"]

def draw_shape(num_sides):
    for j in range(num_sides):
        angle=360/num_sides
        my_turtle.forward(100)
        my_turtle.right(angle)

for i in range(3,11):
    my_turtle.color(random.choice(random_color))
    draw_shape(i)



screen=Screen()
screen.exitonclick()