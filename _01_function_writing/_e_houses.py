"""
Have the turtle draw a row of houses.
"""
import random
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    Window = Tk()
    Window.withdraw()
    # TODO)
    #   1) Move the turtle to the left side of the window near the bottom.
    #   2) Draw ONE flat-topped house with height=100 and green grass after it.
    #   3) Put the code that drew the house into a function called draw_house
    #      HINT: Only the code that draws one house should go in this function.
    #   4) Using the function you just created, draw 10 houses.
    #      HINT: Use a for loop.
    #   5) Run the code to make sure it works before proceeding.
    #   6) Now change the draw_house function to take height as a parameter.
    #   7) Use random numbers to draw 9 houses of different heights.
    #   8) Run the code to make sure it works before proceeding.
    #   9) Make the draw_house function's height input a string and set the
    #      height of the house based on the following:
    #         “small”            =  60
    #         “medium”           =  120
    #         “large”            =  250
    #   10) Make two new functions that draw different shaped roofs
    #      (JUST the roof part): draw_pointy_roof, draw_flat_roof
    #   11) By calling the correct "roof" function, make large houses have
    #      flat roofs and all the others have pointy roofs.
    pass
import turtle

q = turtle
q.speed(9)
q.bgcolor("green")
r = 0
r = random.randint(1, 3)


def draw_house():
    size = r

    def draw_pointy_roof():
        q.penup()
        if size == 2:
            q.pendown()
            q.left(90)
            q.forward(120)
            q.left(45)
            q.forward(85)
            q.left(90)
            q.forward(85)
            q.left(45)
            q.forward(120)
            q.left(90)
            q.forward(120)
        elif size == 1:
            q.pendown()
            q.left(90)
            q.forward(60)
            q.left(45)
            q.forward(42.5)
            q.left(90)
            q.forward(42.5)
            q.left(45)
            q.forward(60)
            q.left(90)
            q.forward(60)

    def draw_flat_roof():
        q.left(90)
        q.forward(280)
        q.left(90)
        q.forward(250)
        q.left(90)
        q.forward(280)
        q.left(90)
        q.forward(250)

    if size == 1:
        weew = 60
        q.forward(weew / 2)
        q.left(90)
        q.forward(weew)
        q.left(90)
        q.forward(weew)
        q.left(90)
        q.forward(weew)
        q.left(90)
        q.forward(weew)
        draw_pointy_roof()
    if size == 2:
        weew = 120
        q.forward(weew / 2)
        q.left(90)
        q.forward(weew)
        q.left(90)
        q.forward(weew)
        q.left(90)
        q.forward(weew)
        q.left(90)
        q.forward(weew)
        draw_pointy_roof()
    if size == 3:
        weew = 250
        q.forward(weew / 2)
        q.left(90)
        q.forward(weew)
        q.left(90)
        q.forward(weew)
        q.left(90)
        q.forward(weew)
        q.left(90)
        q.forward(weew)
        draw_flat_roof()


turtle.penup()
turtle.goto(-400, 50)
turtle.pendown()
for i in range(5):
    draw_house()
    q.forward(125)
    r = random.randint(1, 3)
turtle.penup()
turtle.goto(-400, -250)
turtle.pendown()
for i in range(5):
    draw_house()
    q.forward(125)
    r = random.randint(1, 3)
