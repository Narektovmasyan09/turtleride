import turtle

# timy = turtle.Turtle()

from turtle import Turtle, Screen
timy = Turtle()
print(timy)
timy.shape("turtle")
timy.color("blue")
timy.forward(200)

import time
time.sleep(3)
timy.backward(100)


my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()