import turtle as t
colors=[(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184),
 (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
 (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102)
, (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

my_turtle=t.Turtle()
my_turtle.colormode(255)
screen=t.Screen()
screen.setworldcoordinates(0, 0, screen.window_width(), screen.window_height())

# Move the turtle to the new origin (bottom-left corner)
my_turtle.penup()
my_turtle.goto(0, 0)
my_turtle.pendown()

for i in range(10):
    for color in colors:
        my_turtle.dot(20,color)
        my_turtle.penup()
        my_turtle.forward(50)












screen.exitonclick()