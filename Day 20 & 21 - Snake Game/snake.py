from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for seg_position in STARTING_POSITION:
            self.add_segment(seg_position)

    def move_forward(self):
        for snake_parts in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[snake_parts - 1].xcor()
            new_y = self.segments[snake_parts - 1].ycor()
            self.segments[snake_parts].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    # def snake_control(self):
    def up(self):
        if self.head.heading() != DOWN:
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

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.pu()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # add a new segment to the snake.
        self.add_segment(self.segments[-1].position())
