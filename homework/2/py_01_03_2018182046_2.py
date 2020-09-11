import turtle
turtle

count = 0
while(count <= 5):
    turtle.penup()
    turtle.goto(0, count*10)
    turtle.pendown()
    turtle.forward(50)
    count = count + 1

turtle.left(90)

count = 0
while(count <= 5):
    turtle.penup()
    turtle.goto(count*10, 0)
    turtle.pendown()
    turtle.forward(50)
    count = count + 1

turtle.exitonclick()
