import turtle

screen = turtle.Screen()        #Type of screen is turtle.Screen

leonardo = turtle.Turtle()

counter = 0

while(counter<12):
    leonardo.forward(50)
    leonardo.left(60)       #Turns left 60 degrees
    leonardo.forward(50)
    leonardo.right(90)
    counter = counter + 1


screen.exitonclick()