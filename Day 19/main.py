from turtle import Turtle,Screen
import random
screen=Screen()
is_race_on=False
screen.setup(width=500, height=400)
colors=["red", "orange", "blue", "purple", "yellow", "green"]
user_bet=screen.textinput(title="Make your bet", prompt="Which one turtle will win the race? Enter a color: ")
y_posn=[-100,-60,-20,20,60,100]
all_turtles=[]


for turtle_index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_posn[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtles in all_turtles:
        if turtles.xcor()>230:
            is_race_on=False
            winner_turtle=turtles.pencolor()
            if winner_turtle==user_bet:
                print(f"You've won, {winner_turtle} has won the race!")

            else:
                print(f"You've lost, {winner_turtle} has won the race!")


        rand_distance=random.randint(0,10)
        turtles.forward(rand_distance)






screen.exitonclick()