import turtle
from turtle import Turtle, Screen
import random

# def move_forwards():
#     tim.forward(10)
#
# screen.listen()
# screen.onkey(key="space", fun=move_forwards)
# screen.exitonclick()

# Etch-A-Sketch
# def move_forward():
#     tim.forward(10)
# def move_backward():
#     tim.backward(10)
# def counter_clockwise():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
# def clockwise():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
# def clear_screen():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=counter_clockwise)
# screen.onkey(key="d", fun=clockwise)
# screen.onkey(key="c", fun=clear_screen)
#
# screen.exitonclick()

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner!")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
