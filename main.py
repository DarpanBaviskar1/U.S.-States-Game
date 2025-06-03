import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")

screen.addshape(r"C:\Python\Udemy Projects\Day_25_CSV\US States Project\blank_states_img.gif")
turtle.shape(r"C:\Python\Udemy Projects\Day_25_CSV\US States Project\blank_states_img.gif")

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
data = pandas.read_csv(r"C:\Python\Udemy Projects\Day_25_CSV\US States Project\50_states.csv")
all_states = data["state"].to_list()
guessed_states = []

while len(guessed_states)<50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Enter the State").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t= turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)

remaining_states=[]

count = 0
for x in all_states:
    for y in guessed_states:
        if(x != y):
            count = count + 1
            if(count == len(guessed_states)):
                remaining_states.append(x)
                count = 0
                

df = pandas.DataFrame(remaining_states)
df.to_csv(r"C:\Python\Udemy Projects\Day_25_CSV\US States Project\remaining_states.csv", index=False)

# turtle.mainloop()
# screen.exitonclick()