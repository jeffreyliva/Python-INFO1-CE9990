"""

tkinter.py

Flag of Denmark

"""


import tkinter

            

#dimensions of entire flag, in pixels
whiteHeight = 50
height = 5 * whiteHeight
width = int(height * 16/10)

root = tkinter.Tk()
root.title("Flag of Denmark")

root.geometry(str(width) + "x" + str(height))

#flag colors

Danishred = "#B22234"
Danishwhite = "#FFFFFF"


canvas = tkinter.Canvas(root, highlightthickness = 0)



def drawPixel(x, y, color):
    """
    Color the pixel at coordinates (x, y).
    """
    assert isinstance(x, int) and isinstance(y, int) and isinstance(color, str)
    canvas.create_rectangle(x, y, x + 1, y + 1, width = 0, fill = color)




y = 0
while y < height:

    x = 0
    while x < width:

        if x < width * 5/16 and y < 2 * whiteHeight:
            drawPixel(x, y, Danishred)
        elif x > width * 7/16 and y < 2 * whiteHeight:
            drawPixel(x, y, Danishred)
        elif x < width * 5/16 and y > 3 * whiteHeight:
            drawPixel(x, y, Danishred)
        elif x > width * 7/16 and y > 3 * whiteHeight:
            drawPixel(x, y, Danishred)

        x += 1
    y += 1


canvas.pack(expand = tkinter.YES, fill = "both")


root.mainloop()
