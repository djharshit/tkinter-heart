import turtle

arrow = turtle.Turtle()

arrow.hideturtle()
arrow.fillcolor('red')
arrow.begin_fill()
arrow.left(45)
arrow.forward(100)
arrow.circle(50, 180)
arrow.right(90)
arrow.circle(50, 180)
arrow.forward(100)
arrow.end_fill()

turtle.done()
