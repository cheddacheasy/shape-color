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

r, g, b = input("Canvas color must be RGB format. Ranging from 0, 0,0 to 255, 255, 255").split()
colors=[]
colors.append(int(r))
colors.append(int(g))
colors.append(int(b))

inst = Canvas(width=int(w), height=int(h), color=colors)
inst.makeImage("canvas.png")

print("Which shape would you like to color on your canvas?")
print("Press 1 for square")
print("Press 2 for rectangle")
print("Press 3 to quit")
shape = int(input("--> "))
print()
print()
while shape !=3:

    if shape == 1:
        print("You chose to create a square")
        xaxis, yaxis, side= input("Enter the information in the order X-axis, Y-axis, side length: ").split()



        # make sure xaxis, yaxis, and side length are numbers
        xaxis = int(xaxis)
        yaxis = int(yaxis)
        side = int(side)

        scolor = []
        red = int(input("How much red for your shape: "))
        blue = int(input("How much blue for your shape: "))
        green = int(input("How much green for your shape: "))

        square1 = Sqaure(Xaxis=xaxis,Yaxis=yaxis, SideLength=side, Color=(red, blue, green))

        # we built the canvas and the shape
        # next we need to create the image
        square1.draw(inst)
        inst.makeImage('square.png')

        # loop exit
        print("Which shape would you like to color on your canvas?")
        print("Press 1 for square")
        print("Press 2 for rectangle")
        print("Press 3 to quit")
        shape = int(input("--> "))

    elif shape == 2:
        print("You chose to create a rectangle")
        xaxis, yaxis, rwidth, rheight, rectcolor = input(
            "Enter the information in the order X-axis, Y-axis, height, length, and color").split()
        # make sure xaxis, yaxis, height, and width lengths are numbers
        xaxis = int(xaxis)
        yaxis = int(yaxis)
        rwidth = int(rwidth)
        rheight = int(rheight)

        red = int(input("How much red for your shape: "))
        blue = int(input("How much blue for your shape: "))
        green = int(input("How much green for your shape: "))

        rect1 = Rectangle(Xaxis=xaxis, Yaxis=yaxis, Width=rwidth, Height=rheight, Color=(red, blue, green))

        # we built the canvas and the shape
        # next we need to create the image
        rect1.draw(inst)
        inst.makeImage('rectangle.png')
        # loop exit
        print("Which shape would you like to color on your canvas?")
        print("Press 1 for square")
        print("Press 2 for rectangle")
        print("Press 3 to quit")
        shape = int(input("--> "))

    elif shape == 3:
        print("Thank you for using the color simulator."
              "Have a nice day")
