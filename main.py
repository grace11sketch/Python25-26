from myfunctions import *
from random import randint
turtle.colormode(255)

bob.speed(0)
bob.width(5)

'''
for times in range( num ):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    border = (r,g,b)
    fill = (r,g,b)
    x = randint(-300, 300)
    y = randint(-300, 300)
    radius = randint(5, 30)
    triangle(radius, border, fill )
    jump(x,y)
    
turtle.bgcolor("white")
num = randint(0,255)

for times in range( 256 ):
    c = ( 0, times, 0)
    polygon(4, 100, c)
    bob.left(4)
    bob.forward(10)
    
num = randint(0, 255)
'''


def num():

    turtle.bgcolor("cyan")
num = randint(2,0)
border = "red"
fill = (255, 255, 0)

for times in range( num ):
    circle(20, border, fill )
    bob.forward(50)
    bob.right(15)
