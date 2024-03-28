import colorgram
import turtle as turtle_module
import random

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)


turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
color_list = [(222, 231, 238), (203, 159, 122), (129, 173, 192), (136, 180, 156), (201, 139, 153), (223, 202, 131), (41, 114, 147), (138, 88, 65), (153, 64, 81), (207, 76, 95), (51, 126, 92), (232, 166, 177), (214, 86, 69), (231, 172, 163), (165, 207, 186), (67, 161, 122), (176, 152, 55), (44, 159, 185), (158, 29, 46), (20, 94, 66), (161, 205, 214), (13, 48, 75), (70, 40, 30), (21, 60, 45), (70, 34, 48), (131, 38, 32), (180, 188, 210)]

number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = turtle_module.Screen()
screen.exitonclick()
