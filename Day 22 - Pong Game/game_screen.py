import turtle
from turtle import Turtle

STARTING_POSITION = [(0, -160), (0, -180), (0, -200)]


class GameScreen(Turtle):

    def __init__(self):
        super().__init__()
        self.screen.setup(height= 600, width= 800)
        self.screen.title("Pong Game")
        self.screen.bgcolor("black")
        self.screen.exitonclick()

        self.segments = []
        self.head = self.segments[90]
        self.draw_border()

    def draw_border(self):
        for seg_position in STARTING_POSITION:
            self.add_segment(seg_position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.pu()
        new_segment.goto(position)
        self.segments.append(new_segment)
