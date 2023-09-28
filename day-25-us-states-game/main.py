import turtle
import pandas

screen = turtle.Screen()
screen.title("US STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_data = pandas.read_csv("50_states.csv")
state_list = state_data.state.to_list()
state_name = turtle.Turtle()
state_name.penup()
state_name.hideturtle()
state_name.speed("fastest")

title = f"Guess the state"
correct_guesses = []


while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=title, prompt="What's another state's name").title()

    if answer_state == "Exit":
        break
    if answer_state in state_list:
        correct_guesses.append(answer_state)
        state = state_data[state_data.state == answer_state]
        xcor = int(state.x)
        ycor = int(state.y)
        state_name.goto(xcor, ycor)
        state_name.write(f"{answer_state}")
        title = f"{len(correct_guesses)}/50 States Correct"

states_to_learn = [state for state in state_list if state not in correct_guesses]

# for state in state_list:
#     if state not in correct_guesses:
#         states_to_learn.append(state)

df = pandas.DataFrame(states_to_learn)
df.to_csv("states_to_learn.csv")



