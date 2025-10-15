from turtle import *

UP=90
DOWN=270
LEFT=180
RIGHT=0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
            self.segments=[]
            self.create_snake()
            self.head=self.segments[0]

    def create_snake(self):
        for posit in STARTING_POSITIONS:
            self.add_segment(posit)

    def add_segment(self, posit):
        new_object = Turtle("square")
        new_object.color("white")
        new_object.penup()
        new_object.goto(posit)
        self.segments.append(new_object)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset_game(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() !=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)