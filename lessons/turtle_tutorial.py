"""Lesson on using turtle graphics in Python."""

from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

# leo.forward(50)
# leo.left(30)
# leo.right(40)

# done()

# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# leo.forward(300)

# done()

leo.penup()
leo.goto(-90, -90)
leo.pendown()

leo.fillcolor(36, 155, 145)
leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1

leo.end_fill()  

leo.color(99, 204, 250)
leo.color("green", "yellow")
# leo.begin_fill()
# # code for shape to be filled
# leo.end_fill()

#leo.speed(50)
#leo.hideturtle()



bob: Turtle = Turtle()
bob.color("black", "black")

bob.penup()
bob.goto(-90, -90)
bob.pendown()
bob.speed(200)

side_length: float = 300
j: int = 0
while j < 100:
    leo.forward(side_length)
    leo.left(121)
    side_length = side_length * 0.97
    j = j + 1


done()
