from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DIRECTIONS = {
    "right": 0,
    "up": 90,
    "down": 270,
    "left": 180
}


class Snake:

    def __init__(self):
        self.segments = []
        self.__create_snake()
        self.head = self.segments[0]

    def __create_snake(self):
        for position in STARTING_POSITION:
           self.create_segment(position)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            next_x = self.segments[i - 1].xcor()
            next_y = self.segments[i - 1].ycor()
            self.segments[i].goto(next_x, next_y)
        self.head.forward(MOVE_DISTANCE)

    def change_direction(self, direction):
        angle = DIRECTIONS[direction]
        if abs(self.head.heading() - angle) != 180:
            self.head.setheading(angle)

    def add_segment(self):
        last = self.segments[-1]
        self.create_segment((last.xcor(),last.ycor()))

    def create_segment(self,position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

