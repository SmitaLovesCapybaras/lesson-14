import turtle
turtle.Screen().bgcolor("Orange")
turtle.Screen().setup(300,400)
square=turtle.Turtle()
num_sides=4
side_length=1000
angle=360.0/num_sides
for i in range(num_sides):
    square.forward(side_length)
    square.right(angle)
turtle.done()