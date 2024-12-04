import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "kerala_image (1).gif"
screen.addshape(image)        #to show the image of map
turtle.shape(image)

#def get_mouse_click_coor(x, y):
#    print(x, y)
#
#turtle.onscreenclick(get_mouse_click_coor)

data = pandas.read_csv("14_districts.csv")
all_states = data.district.to_list()  #to_list done to use in keyword in if
guessed_district = []

while len(guessed_district)<14 :
    answer_district = screen.textinput(title=f"{len(guessed_district)}/14 states correct",
                                       prompt="Whats another district name?").title()   #whatever entered  bcms "Bsdfc" form
    if answer_district == "Exit":
        missing_district = [district for district in all_states if district not in guessed_district]
        #missing_states = []
        #for state in all_states:
        #    if state not in guessed_states:
        #        missing_states.append(state)
        new_data = pandas.DataFrame(missing_district)
        new_data.to_csv("districts_to_learn.csv")
        break;
    if answer_district in all_states:
        guessed_district.append(answer_district)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        district_data = data[data.district == answer_district]
        t.goto(district_data.x.item(), district_data.y.item())  #item() just picks the data element
        t.write(answer_district)




     #to keep screen there even after completing code



