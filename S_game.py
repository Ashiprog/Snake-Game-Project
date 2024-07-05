from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT= 0

class S_game:
    def __init__(self):
        self.segments = []
        self.create_s()
        self.head=self.segments[0]


    def create_s(self):
        for positions in STARTING_POSITIONS:
            new_s = Turtle("square")
            new_s.color("white")
            new_s.penup()
            new_s.goto(positions)
            self.segments.append(new_s)

    def move_s(self):
        for seg in range(len(self.segments)-1,0,-1):
            x_cor = self.segments[seg-1].xcor()
            y_cor = self.segments[seg-1].ycor()
            self.segments[seg].goto(x_cor,y_cor)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!= DOWN:
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






