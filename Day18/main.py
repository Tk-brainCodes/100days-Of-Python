import colorgram
import random
import turtle as t

tim = t.Turtle()
t.colormode(255)
tim.penup()
tim.hideturtle()

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# """Get the color out in terminal"""
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.b
#     b = color.rgb.b
#     color_list = (r,g,b)
#     rgb_colors.append(color_list)
# 
# print(rgb_colors)

colors_list = [(254, 252, 252), (232, 243, 243), (253, 245, 245), (43, 176, 176), (79, 174, 174), (226, 109, 109), (230, 253, 253), (160, 82, 82), (4, 101, 101), (3, 64, 64), (246, 127, 127), (109, 247, 247), (252, 53, 53), (184, 251, 251), (211, 5, 5), (35, 252, 252), (177, 248, 248), (139, 0, 0), (252, 35, 35), (50, 56, 56), (216, 171, 171), (16, 144, 144), (85, 252, 252), (188, 109, 109), (23, 107, 107), (8, 215, 215), (99, 50, 50), (231, 205, 205), (204, 35, 35), (112, 4, 4)]

tim.setheading(200)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
tim.speed("fastest")


for dot_count in range(1,number_of_dots + 1):
    tim.dot(20, random.choice(colors_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = t.Screen()
screen.exitonclick()