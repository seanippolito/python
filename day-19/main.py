from turtle import Turtle, Screen
import random

colors = ["red", "blue", "green", "yellow", "pink", "purple"] 
screen = Screen()
screen.setup (width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which tutle will win the race? Enter a color: ")

y_positions = [-100, -50, 0, 50, 100, 150]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True 

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            print(f"The {turtle.pencolor()} turtle has won!")
            if turtle.pencolor() == user_bet:
                print("You've won!")
            else:
                print("You've lost!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.listen()

screen.exitonclick()