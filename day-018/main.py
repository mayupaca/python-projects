from turtle import Turtle, Screen
import turtle as t
import random

tim = Turtle()
t.colormode(255)


# Create random RGB color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim.speed("fastest")
tim.hideturtle()
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
        tim.color(random_color())

draw_spirograph(5)

#######################################################################
# directions = [0, 90, 180, 270]
# tim.pensize(10)
# tim.speed("fastest")
#
# for _ in range(100):
#     tim.color(random_color())
#     tim.setheading(random.choice(directions))
#     tim.forward(30)

# Python Tuples = a list that you can not change(immutable)
# my_tuple = (1, 3, 8)
# list(my_tuple) # タプルから配列にする

# moves = [tim.forward(50), tim.right(90), tim.left(90)]
# def draw_move():
#     coin_toss = random.randint(0, 1)
#     if coin_toss == 0:
#         tim.right(90)
#     else:
#         tim.left(90)
#     tim.forward(50)
#
# for i in range(100):
#     tim.color(random.choice(colors))
#     tim.pensize(10)
#     draw_move()

######################################################
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)

# for corner in range(3, 11):
#     degree = 360 / corner
#
#     for i in range(corner):
#         tim.forward(100)
#         tim.right(degree)
#######################################################
# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# tim.shape("turtle")
# tim.color("coral")
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
#  .right(90)

# screen = Screen()
# screen.exitonclick()

# 長いモジュール名を短くする
# import turtle_sdf_sd_sdr_SD as t
# tim = t.Turtle()

# from turtle import *
# モジュールの中の全てをインポートする
# 　どのモジュールからインポートしてるのかわからなくなるのであまり使わないようにする
