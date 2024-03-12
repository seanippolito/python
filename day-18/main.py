import turtle as t
from data import colors
import random


tim = t.Turtle()
tim.color("white")
tim.setx(-100)
tim.sety(500)
tim.speed("fastest")
tim.shape("turtle")



def draw_shape(num_sides):
    for _ in range(num_sides):
        tim.color(random.choice(colors))
        angle = 360 / num_sides
        tim.forward(100)
        tim.right(angle)

for i in range(2, 100):
    draw_shape(i)