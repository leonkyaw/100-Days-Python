#  to extract color from the image and saved each color as tuple and collection as list.

# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
#
# color_palette = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_palette.append((r, g, b))
#
# print(color_palette)

# TODO 1: 10x10 painting
# TODO 2: dot is 20 in size and spacing is 50
# TODO 3: How to move the arrow to draw 10x10

import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed('fastest')
tim.hideturtle()

color_list = [(241, 244, 248), (5, 12, 35), (40, 21, 16), (130, 89, 54), (202, 137, 119),
              (235, 211, 82), (188, 137, 161), (216, 83, 67), (80, 6, 20), (33, 139, 65),
              (147, 86, 105), (193, 77, 101), (29, 87, 29), (220, 176, 210), (74, 107, 141),
              (152, 136, 65), (20, 207, 180), (12, 72, 28), (132, 158, 180), (7, 62, 139),
              (114, 188, 158), (86, 133, 173), (125, 8, 28), (18, 204, 220), (242, 204, 6),
              (236, 172, 164), (133, 223, 208)]

tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for number_of_dots in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if number_of_dots % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)  # going back to the starting point
        tim.setheading(0)  # point the arrow to the left








screen = t.Screen()
screen.exitonclick()
