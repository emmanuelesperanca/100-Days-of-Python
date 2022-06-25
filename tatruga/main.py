# from turtle import Turtle, Screen
# import prettytable

# timmy = Turtle()
# my_screen = Screen()
# print(my_screen.canvheight)
# timmy.shape('turtle')
# timmy.color('black', 'aquamarine')
# timmy.pen(pencolor="green", fillcolor="black", pensize=10, speed=9)
# timmy.begin_fill()
# n = 10
# while n <= 40:
#     timmy.circle(n)
#     timmy.speed(10)
#     n = n+10
# timmy.end_fill()
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon", ["Bulbasauro", "Squirtle", "Charmander"])
table.add_column("Type", ["Grass", "Water", "Fire"])
table.align["Pokemon"] = "l"
table.align["Type"] = "l"

print(table)

