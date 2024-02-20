from turtle import *

width(5)



speed(500)

penup()
goto(-300, -100)
pendown()

color("brown")
begin_fill()
forward(150)
left(90)
forward(150)
left(90)
forward(150)
left(90)
forward(150)
end_fill()

penup()
goto(-150, 50)
pendown()

color("red")
begin_fill()
right(150)
forward(150)
left(120)
forward(150)
end_fill()

penup()
goto(-250, -100)
pendown()

color("black")
begin_fill() 
right(150)
forward(65)
right(90)
forward(50)
right(90)
forward(65)
end_fill()

penup()
goto(-275, -10)
pendown()

color("light blue")
begin_fill()
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)

penup()
goto(-210, -10)
pendown()

left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
end_fill()

#first house painted

penup()
goto(-130, -100)
pendown()

color("black")
begin_fill()
left(90)
forward(150)
left(90)
forward(150)
left(90)
forward(150)
left(90)
forward(150)
end_fill()

penup()
goto(20, 50)
pendown()

color("yellow")
begin_fill()
right(150)
forward(150)
left(120)
forward(150)
end_fill()

penup()
goto(-80, -100)
pendown()

color("brown")
begin_fill() 
right(150)
forward(65)
right(90)
forward(50)
right(90)
forward(65)
end_fill()

penup()
goto(-105, -10)
pendown()

color("light blue")
begin_fill()
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)

penup()
goto(-40, -10)
pendown()

left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
end_fill()

#second house painted

penup()
goto(40, -100)
pendown()

color("red")
begin_fill()
left(90)
forward(150)
left(90)
forward(150)
left(90)
forward(150)
left(90)
forward(150)
end_fill()

penup()
goto(190, 50)
pendown()

color("black")
begin_fill()
right(150)
forward(150)
left(120)
forward(150)
end_fill()

penup()
goto(90, -100)
pendown()

color("green")
begin_fill() 
right(150)
forward(65)
right(90)
forward(50)
right(90)
forward(65)
end_fill()

penup()
goto(65, -10)
pendown()

color("light blue")
begin_fill()
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)

penup()
goto(130, -10)
pendown()

left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
end_fill()


#third house painted


penup()
goto(270, -100)
pendown()

color("brown")
begin_fill()
left(90)
forward(10)
left(90)
forward(200)
left(90)
forward(10)
left(90)
forward(200)
right(180)
forward(200)
right(90)
end_fill()

color("green")
begin_fill()
circle(40)
end_fill()

penup()
goto(300, 130)
pendown()

begin_fill()
circle(40)
end_fill()

penup()
goto(240, 130)
pendown()

begin_fill()
circle(40)
end_fill()

penup()
goto(270, 180)
pendown()

begin_fill()
circle(40)
end_fill()

#tree painted

penup()
goto(30, 200)
pendown()

color("orange")
begin_fill()
circle(60)
end_fill()

#sun painted

penup()
goto(-1000, -100)
pendown()

color("green")
begin_fill()
goto(1000, -100)
goto(1000, - 1000)
goto(-1000, -1000)
end_fill()

#grass painted


exitonclick()

