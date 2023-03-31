from turtle import *

bgcolor("black")
speed(5000000000000)
hideturtle()
for i in range (120):
    color("red")
    circle(i)
    color("orange")
    circle(i*2)
    right(3)
    forward(3)
done()