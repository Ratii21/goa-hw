from turtle import *

#changing cursor speed
speed(3)

#changing line width
width(5)

#changing cursor shape
shape("turtle")

#painting walls
color("black")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
end_fill()

#painting door
left(90)
forward(80)
color("brown")
begin_fill()
left(90)
forward(100)
right(90)
forward(40)
right(90)
forward(100)
end_fill()

#paintin roof
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(135)
forward(142)
left(90)
forward(142)
end_fill()

#painting windows
penup()
goto(20, 180)
pendown()

color("light blue")
begin_fill()
left(45)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)

penup()
goto(120, 180)
pendown()

left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
end_fill()

#result is painted house

exitonclick()
