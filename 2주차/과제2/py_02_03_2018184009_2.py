import turtle
turtle.penup()
turtle.goto(-450,-200)

count=0
count2=0
while(count<6):
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    count=count+1
    turtle.goto(-450,-200+count*100)

turtle.goto(-450,-200)
turtle.left(90)
while(count2<6):
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    count2=count2+1
    turtle.goto(-450+count2*100,-200)








turtle.exitonclick()
