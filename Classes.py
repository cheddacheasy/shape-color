'''

Contains our classes to create our classes that will be imported to the main,py file

'''
import numpy as np
from PIL import Image

class Canvas:

    """
    This is the background that will hold the shapes. It will need
    inputs such as the width, height, and color. It also produces the image
    including the shapes at the end
    """

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.data[:] = [self.color]

    def makeImage(self, imgpath):
        img = Image.fromarray(self.data, 'RGB')
        img.save(imgpath)




class Sqaure:
    """
    takes in coordinates, size, and color to build the square that will
    be put on the canvas
    """



    def __init__(self, Xaxis, Yaxis, SideLength, Color):
        self.Xaxis = Xaxis
        self.Yaxis = Yaxis
        self.SideLength = SideLength
        self.Color = Color

    def draw(self, canvas):
        canvas.data[self.Xaxis: self.Xaxis + self.SideLength, self.Yaxis: self.Yaxis + self.SideLength] = self.Color

class Rectangle:
    """
        takes in coordinates, size, and color to build the rectangle that will
        be put on the canvas
        """


    def __init__(self, Xaxis, Yaxis, Width, Height, Color):
        self.Xaxis = Xaxis
        self.Yaxis = Yaxis
        self.Height = Height
        self.Width = Width
        self.Color = Color

    def draw(self, canvas):
        canvas.data[self.Xaxis: self.Xaxis + self.Width, self.Yaxis: self.Yaxis + self.Height,] = self.Color



# canvas = Canvas(height=50, width=30, color=(255, 255, 255))
#
# s1 = Sqaure(Xaxis=25, Yaxis=15, SideLength=5, Color=(0, 0,0))
#
# s1.draw(canvas)
#
# canvas.makeImage('canvas2.png')