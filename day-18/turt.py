import turtle as t
from data import colors
import random


my_tuple = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.shape("turtle")


tom = t.Turtle()
tom.speed("fastest")
tom.shape("turtle")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple = (r, g, b)
    return my_tuple

def random_walk():
    for _ in range(200):
        tim.color(random_color())
        tim.shapesize(1, 1, 5)
        tim.pensize(10)
        tim.setheading(random.choice([0, 90, 180, 270]))
        tim.forward(30)



def draw_shape(num_sides):
    for _ in range(num_sides):
        tom.color(random_color())
        angle = 360 / num_sides
        tom.forward(100)
        tom.right(angle)

def draw_shapes():
    for i in range(2, 100):
        draw_shape(i)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tom.color(random_color())
        tom.circle(100)
        tom.setheading(tom.heading() + size_of_gap)

draw_spirograph(5)
random_walk()
draw_shapes()