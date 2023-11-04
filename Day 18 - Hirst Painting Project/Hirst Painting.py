# import colorgram
#
# colors = colorgram.extract('537b6eca8c43b46982da4c2af786fb1124592d0a-1200x995.jpg', 30)
# print(colors)
#
# rgb_colors = []
# for color in colors:
#     response = color.rgb.response
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (response, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

rgb_colors = [(233, 233, 232), (231, 233, 238), (237, 231, 234), (221, 232, 225), (208, 160, 82), (55, 89, 132),
              (145, 91, 40), (139, 26, 48), (222, 207, 105), (132, 176, 203), (45, 55, 104), (158, 46, 84),
              (169, 159, 40), (128, 189, 143), (84, 20, 44), (38, 43, 66), (187, 93, 106), (188, 138, 167),
              (84, 123, 182), (59, 39, 30), (79, 153, 165), (88, 157, 90), (195, 80, 71), (159, 201, 220), (79, 74, 43),
              (45, 74, 77), (59, 127, 118), (218, 176, 187), (167, 207, 165), (179, 188, 212)]

from turtle import Turtle, Screen, colormode
import random

init_x = -200
init_y = -200

tim = Turtle()
tim.pu()
tim.hideturtle()
tim.speed(0)
colormode(255)


def paint_row():
    for _ in range(10):
        tim.dot(20, random.choice(rgb_colors))
        tim.fd(50)


def position():
    for _ in range(20, 400, 40):
        tim.goto(init_x, init_y + _)
        paint_row()


position()

screen = Screen()
screen.exitonclick()
