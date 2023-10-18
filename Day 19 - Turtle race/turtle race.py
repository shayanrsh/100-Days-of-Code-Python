from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


all_turtles = []
for turtle_index in range(6):
    all_turtles.append(Turtle(shape="turtle"))
    all_turtles[turtle_index].pu()
    all_turtles[turtle_index].color(colors[turtle_index])
    all_turtles[turtle_index].goto(x=-230, y=-180 + 50 * (turtle_index + 1))


if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
