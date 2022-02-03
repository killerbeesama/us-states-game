from turtle import Screen, Turtle
import turtle
import pandas as pd

image = "./us-states-game-start/blank_states_img.gif"
screen = Screen()
screen.addshape(image)
turtle.shape(image)

correctly_guessed = []
left_answers = []
count = 0 
data = pd.read_csv("us-states-game-start/50_states.csv")
state_data = data['state']
game_on = True
while game_on:
    if len(correctly_guessed) == 50:
        game_on = False
        print("you answerd all correctly")
    else:
        answer = screen.textinput(f"{count}/50","guess the state").title()
        if answer == "Exit":
            for i in state_data:
                if i not in correctly_guessed:
                    left_answers.append(i)
            df = pd.DataFrame(left_answers)
            df.to_csv('us-states-game-start/ans.csv')
            game_on = False
        elif answer in correctly_guessed:
            print("you already gussed it.Try another guess")
        else:
            for i in state_data:
                if i == answer:
                    t = Turtle()
                    t.hideturtle()
                    t.penup()
                    correctly_guessed.append(i)
                    count += 1
                    location_data = data[data['state'] == answer]
                    t.goto(int(location_data['x']),int(location_data['y']))
                    t.write(answer)
                    


# screen.exitonclick()