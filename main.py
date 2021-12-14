from Classes import Canvas, Sqaure, Rectangle

import numpy as np
from PIL import Image



"""
CLI
"""


print("Hello welcome to math painter")
print("Please enter the following for your canvas:")

w = input("width: ")
h = input("height: ")

r, g, b = input("color in RGB: ").split()
color=[]
color.append(int(r))
color.append(int(g))
color.append(int(b))
print(color)
inst = Canvas(int(w), int(h), color)

print("Which shape would you like to color on your canvas?")
shape = int(input("Press 1 for square and press 2 for rectangle"))

if shape == 1:
    print("You chose to create a square")
    xaxis, yaxis, side= input("Enter the information in the order X-axis, Y-axis, side length: ").split()



    # make sure xaxis, yaxis, and side length are numbers
    xaxis = int(xaxis)
    yaxis = int(yaxis)
    side = int(side)

    scolor = []
    n = 3
    for i in range(0,n):
        z = int(input("Enter the color of the square in RGB: "))
        scolor.append(z)

    square1 = Sqaure(xaxis,yaxis, side, scolor)

    # we built the canvas and the shape
    # next we need to create the image
    square1.draw(inst)
    inst.makeImage('square.png')

else:
    print("You chose to create a rectangle")
    xaxis, yaxis, rwidth, rheight, rectcolor = input(
        "Enter the information in the order X-axis, Y-axis, height, length, and color").split()
    # make sure xaxis, yaxis, height, and width lengths are numbers
    xaxis = int(xaxis)
    yaxis = int(yaxis)
    rwidth = int(rwidth)
    rheight = int(rheight)

    rect1 = Rectangle(xaxis, yaxis, rwidth, rheight, rectcolor)

    # we built the canvas and the shape
    # next we need to create the image
    rect1.draw(inst)
    inst.makeImage('rectangle.png')
