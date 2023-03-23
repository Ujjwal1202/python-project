# $ python -m pip install turtle
# Importing the Required Module
# pip install turtle
import turtle

# Create window to Display raintbow Benzene
window = turtle.Screen()

# Setting Geomentry for the window
window.setup(600, 600, startx=0, starty=100)

# Colours
colors = ['red', 'purple', 'blue', 'green', 'orange','yellow']

# To draw the rainbow Benzene
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(280):
    t. pencolor(colors [x%6])
    t.width(x//90 + 1)
    t. forward(x)
    t. left(59)

    