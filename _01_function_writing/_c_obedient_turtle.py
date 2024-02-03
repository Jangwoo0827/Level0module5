"""
Make an obedient turtle that will obey commands to draw shapes.
"""
from tkinter import messagebox, simpledialog, Tk
import turtle

if __name__ == '__main__':
    # TODO)
    #   1. Create a turtle.
    #   2. Write 3 method definitions for drawing a square, triangle, and
    #      circle.
    #   3. Ask the user for the for a shape to draw.
    #   4. Draw the appropriate shape depending on their answer (call the right
    #      function)
    pass

import turtle

q = turtle
q.speed(10)

w = simpledialog.askstring(title=None, prompt="What shape you want to draw?(square or triangle or circle)")
e = simpledialog.askinteger(title=None, prompt="How long?")


def square(side):
    q.clear()
    for a in range(16):
        q.forward(side)
        q.right(90)


def triangle(side):
    q.clear()
    for a in range(12):
        q.forward(side)
        q.right(120)


def circle(radius):
    q.clear()
    for a in range(4):
        q.circle(radius)


if w == "square":
    square(e)
if w == "triangle":
    triangle(e)
if w == "circle":
    circle(e)
exit()
