# import colorgram,
#
# colors = colorgram.extract("image.jpg", 30)

# rgb_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_list.append(new_color)
#
# print(rgb_list)

from turtle import Turtle, Screen
import random

tim = Turtle()

color_list = [(197, 165, 117), (142, 80, 56), (220, 201, 137), (59, 94, 119), (164, 152, 53), (136, 162, 181), (131, 34, 22), (69, 39, 32), (53, 117, 86), (192, 95, 78), (146, 177, 149), (19, 91, 68), (165, 143, 157), (31, 59, 76), (111, 75, 81), (228, 176, 164), (128, 29, 33), (179, 204, 177), (71, 34, 36), (25, 82, 89), (89, 146, 127), (18, 69, 57), (41, 66, 90), (219, 178, 182), (175, 94, 98), (179, 192, 205)]


for row in range(1, 11):
    tim.penup()
    tim.forward(50)
    tim.dot(20)

# tim.right(90)
# tim.forward(80)
# tim.right(90)

    for column in range(2, 11):
        tim.penup()
        tim.forward(80)


# column

tim_screen = Screen()
tim_screen.exitonclick()
