import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
score = 0

while score < 50:
  answer_state = screen.textinput(f"{score} / 50", "Name a U.S. state:").title()
  if answer_state == "Exit":
    missing_states = []
    for state in all_states:
      if state not in guessed_states:
        missing_states.append(state)
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv("states.to.learn.csv")
    break
  elif answer_state in all_states:
      placement = turtle.Turtle()
      placement.hideturtle()
      placement.penup()
      state_row = data[data.state == answer_state]
      placement.goto(int(state_row.x), int(state_row.y))
      placement.write(answer_state)
      guessed_states.append(answer_state)
      score += 1

