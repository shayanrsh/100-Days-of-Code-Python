from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.move_x_axis = 10
        self.move_y_axis = 15
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.move_x_axis, self.ycor() + self.move_y_axis)

    def bounce_y(self):
        self.move_y_axis *= -1

    def bounce_x(self):
        self.move_x_axis *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
