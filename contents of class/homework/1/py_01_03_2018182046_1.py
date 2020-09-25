import turtle
turtle

turtle.shape('turtle')



def draw_bieup():
	turtle.pendown()
	turtle.right(90)
	turtle.forward(50)
	turtle.right(90)
	turtle.forward(50)
	turtle.right(90)
	turtle.forward(50)
	turtle.left(180)
	turtle.forward(25)
	turtle.left(90)
	turtle.forward(50)
	turtle.penup()

def draw_ah():
	turtle.pendown()
	turtle.left(90)
	turtle.forward(25)
	turtle.left(180)
	turtle.forward(50)
	turtle.left(180)
	turtle.forward(25)
	turtle.right(90)
	turtle.forward(25)
	turtle.penup()

def draw_giyeok():
	turtle.pendown()
	turtle.forward(50)
	turtle.right(90)
	turtle.forward(50)
	turtle.penup()

def draw_hieut():
	turtle.pendown()
	turtle.forward(15)
	turtle.left(90)
	turtle.forward(25)
	turtle.left(180)
	turtle.forward(50)
	turtle.left(180)
	turtle.forward(25)
	turtle.setheading(-90)
	turtle.penup()
	turtle.forward(50)
	turtle.setheading(0)
	turtle.pendown()
	turtle.circle(15)
	turtle.penup()

def draw_yo():
	turtle.pendown()
	turtle.forward(35)
	turtle.left(180)
	turtle.forward(70)
	turtle.left(180)
	turtle.forward(20)
	turtle.left(90)
	turtle.forward(40)
	turtle.left(180)
	turtle.forward(40)
	turtle.left(90)
	turtle.forward(30)
	turtle.left(90)
	turtle.forward(40)
	turtle.left(180)
	turtle.forward(40)
	turtle.penup()

	
def draw_jieut():
	turtle.pendown()
	turtle.forward(70)
	turtle.right(135)
	turtle.forward(70)
	turtle.left(180)
	turtle.forward(35)
	turtle.right(90)
	turtle.forward(35)
	turtle.penup()

	
def draw_uh():
	turtle.pendown()
	turtle.forward(25)
	turtle.left(90)
	turtle.forward(25)
	turtle.left(180)
	turtle.forward(50)
	turtle.penup()

def draw_ieung():
	turtle.pendown()
	turtle.circle(20)
	turtle.penup()

	
turtle.penup()
turtle.goto(-300,0)
turtle.pendown()

draw_bieup()

turtle.forward(30)

draw_ah()

turtle.right(145)
turtle.penup()
turtle.forward(85)
turtle.setheading(0)
 
draw_giyeok()

turtle.left(150)
turtle.forward(150)
turtle.setheading(-90)

draw_hieut()

turtle.setheading(-90)
turtle.forward(60)
turtle.setheading(0)

draw_yo()

turtle.setheading(0)
turtle.left(70)
turtle.forward(115)
turtle.setheading(0)

draw_jieut()

turtle.left(90)
turtle.forward(25)
turtle.setheading(0)

draw_uh()

turtle.right(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(50)
turtle.setheading(0)

draw_ieung()

turtle.exitonclick()
