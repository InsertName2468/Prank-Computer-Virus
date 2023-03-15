from turtle import *
speed(10) #It is already the fastest speed, don't change it unless you want it to run slower.
color('cyan') #You can change it to any color you want, it won't interrupt the script.
bgcolor('black')#You can change it to any color you want, it won't interrupt the script
b=200
while b > 0:
    left(b)
    forward(b * 3)
    b=b-1
