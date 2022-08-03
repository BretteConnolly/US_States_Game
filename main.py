import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image) #uses map as turtle obect

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list() #list of values from "state" column
guessed_states = []
score = 0

while score < 50: #while not all the states have been guessed
  answer_state = screen.textinput(f"{score} / 50", "Name a U.S. state:").title()
  if answer_state == "Exit":
    missing_states = [state for state in all_states if state not in guessed_states] #states the user did not guess
    new_data = pandas.DataFrame(missing_states) #convert to DataFrame so this list can be stored in a CSV file as a Pandas series
    new_data.to_csv("states.to.learn.csv") #file of missing states provided at the end to educate the user
    break
  elif answer_state in all_states: #state must be one on the list of states
      placement = turtle.Turtle()
      placement.hideturtle()
      placement.penup()
      state_row = data[data.state == answer_state] #row of the guessed state
      placement.goto(int(state_row.x), int(state_row.y)) #coordinate values from this row
      placement.write(answer_state) #labels state name onto map
      guessed_states.append(answer_state)
      score += 1

