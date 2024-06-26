from turtle import Turtle
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments=[]
        self.creat_snake()
        self.head=self.segments[0]
    def creat_snake(self):
        for position in STARTING_POSITIONS:
           self.add_segments(position)
    def add_segments(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.pu()
        new_segment.goto(position)
        self.segments.append(new_segment)
    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.creat_snake()
        self.head = self.segments[0]

    def extend(self):
        # add segments to the snake
        self.add_segments(self.segments[-1].position())
    def move(self):
        for seg_num in range((len(self.segments) - 1), 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)
    def up(self):
        if self.head.heading != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading != LEFT:
            self.head.setheading(RIGHT)

