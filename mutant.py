import turtle

screen = turtle.Screen()        #Type of screen is turtle.Screen
screen.bgcolor('lightgrey')
leonardo = turtle.Turtle()
leonardo.shape("turtle")
leonardo.pensize(2)
leonardo.speed(10)
#counter = 0

for color in ["yellow", "blue", "red", "blue", "white", "blue", "yellow", "blue", "red", "blue", "white", "blue"]:
    leonardo.color(color)
    leonardo.forward(65)
    leonardo.stamp()
    leonardo.left(60)       #Turns left 60 degrees
    leonardo.forward(65)
    leonardo.stamp()
    leonardo.right(90)

leonardo.penup()
leonardo.forward(65)
leonardo.left(90)
leonardo.forward(65)
leonardo.left(90)
leonardo.pendown()

for color in ["yellow", "blue", "red", "blue", "white", "blue", "yellow", "blue", "red", "blue", "white", "blue"]:
    leonardo.color(color)
    leonardo.forward(65)
    leonardo.stamp()
    leonardo.left(60)       #Turns left 60 degrees
    leonardo.forward(65)
    leonardo.stamp()
    leonardo.right(90)

leonardo.right(90)
leonardo.penup()
leonardo.forward(300)
leonardo.pendown()

for counter in range (25):
    leonardo.forward(counter*2)
    leonardo.left(60)

for counter in range(25):
    if counter % 2 == 0:
        leonardo.forward(50)
    leonardo.left(60)


while(counter<12):
    leonardo.forward(50)
    leonardo.left(60)       #Turns left 60 degrees
    leonardo.forward(50)
    leonardo.right(90)
    counter = counter + 1

#for corner in range(6) count from 0 up to and not including 6, number of repeats




screen.exitonclick()