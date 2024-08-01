#This means import everything from vpython
from vpython import *
from time import *

"""
ball=sphere(color=color.red)
sleep(5)
ball.color=color.blue
sleep(5)
ball.color=color.green
"""

#myBox=box(color=color.magenta,length=12,width=1,height=.2)

#myTube=cylinder(color=color.orange,length=12,width=1,radius=1)

floor=box(pos=vector(0,-5,0),color=color.white,length=10,height=.1,width=10)
ceiling=box(pos=vector(0,5,0),color=color.white,length=10,height=.1,width=10)

while True:
    pass