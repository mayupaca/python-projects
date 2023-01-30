# import another_module
# print(another_module.another_variable)

# classの頭文字は大文字
# turtle graphics library
# https://docs.python.org/3/library/turtle.html
# from turtle import Turtle, Screen
#
# # turtle graphics libraryのTurtle classを使って新しい亀オブジェクトを作成
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkOrange")
# timmy.forward(100)
#
# # turtle graphics libraryのScreen classを使って新しいオブジェクトを作成
# my_screen = Screen()
# # my_screen is object and canvheight is attribute associate the object
# print(my_screen.canvheight)
# # function
# # クリックするまで実行されるfunction
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pidgey", "Caterpie", "Pichu"])
table.add_column("Type", ["Flying", "Bug", "Electric"])
table.align = "l"
print(table)
