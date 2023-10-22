import turtle

import pandas as pd

screen = turtle.Screen()
score = 0
screen.title(f"U.S. States Game.")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
my_turtle = turtle.Turtle()
my_turtle.penup()
my_turtle.hideturtle()

data = pd.read_csv("50_states.csv")
guessed_states = []

while score < 50:
    answer_state = screen.textinput(title=f"score {score}/50", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        all_states = data.state.to_list()
        not_guessed_states = [x for x in all_states if x not in guessed_states]
        missing_states = pd.DataFrame(not_guessed_states)

        missing_states.to_csv("missing_states.csv")
        break
    if answer_state in data['state'].values:
        guessed_states.append(answer_state)
        score += 1
        # Filter the DataFrame for the state 'California'
        california_data = data[data['state'] == answer_state]

        # Get the 'x' and 'y' values for California
        x = california_data['x'].values[0]
        y = california_data['y'].values[0]

        my_turtle.goto(x, y)
        my_turtle.write(answer_state)
        screen.title(f"U.S. States Game. Current score {score}/50")
