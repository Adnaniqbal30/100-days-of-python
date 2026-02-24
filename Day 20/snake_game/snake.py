from turtle import Turtle
class Snake:
    def __init__(self):
        starting_posn=[(0, 0),(-20, 0),(-40, 0)]
        segments=[]
        for posn in starting_posn:
            new_segments=Turtle()
            new_segments.color("white")
            new_segments.shape("square")
            new_segments.penup()
            new_segments.goto(posn)
            segments.append(new_segments)

        for seg_num in range(len(segments) - 1, 0, -1):
            new_x = segments[seg_num - 1].xcor()
            new_y = segments[seg_num - 1].ycor()
            segments[seg_num].goto(new_x, new_y)

        segments[0].forward(10)
