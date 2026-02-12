from turtle import Turtle,Screen
timmy=Turtle()
print(timmy)
#here timmy is an object we created from class turtle
#shapes,color,forward are the methods
timmy.shape("turtle")
timmy.color("brown1")
timmy.forward(100)
#canvaheight is the attribute
my_screen=Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
