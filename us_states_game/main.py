import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)        #to show the image of map
turtle.shape(image)

#def get_mouse_click_coor(x, y):
#    print(x, y)
#
#turtle.onscreenclick(get_mouse_click_coor)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()  #to_list done to use in keyword in if
guessed_states = []

while len(guessed_states)<50 :
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct",
                                    prompt="Whats another states name?").title()   #whatever entered  bcms "Bsdfc" form
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        #missing_states = []
        #for state in all_states:
        #    if state not in guessed_states:
        #        missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break;
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())  #item() just picks the data element
        t.write(answer_state)




     #to keep screen there even after completing code

