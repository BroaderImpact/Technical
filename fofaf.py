# from visual import *
from __future__ import division 
from vpython import * 
import random
import numpy as np
import matplotlib.pyplot as plt
import math
baseball = sphere(pos=vector(-4,-2,5), radius=0.20, color=color.white)
tennisball = sphere(pos=vector(3,1,-2), radius=0.15, color=color.green) 
#arrow(pos=vector(2,-3,0), axis=vector(3,4,0), color=color.cyan) 
arrow(pos=baseball.pos, axis=tennisball.pos-baseball.pos, color=color.red)
print (tennisball.pos)
t = 0
while t<10:
    t = t+0.5
    print(t) 
print("End of program") 
theta = 0
while theta<2*pi:
    theta = theta+(pi/5)
    print (theta)
print("Real End!")
