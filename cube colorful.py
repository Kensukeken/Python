import turtle
import random

# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("black")

# Create a new turtle to draw our pattern
my_turtle = turtle.Turtle()
my_turtle.speed(10)

# This function draws a rectangle of a certain size and color
def draw_rectangle(turtle, size):
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)

# This function draws a colorful spiral of rectangles
def draw_spiral(turtle, size):
    for _ in range(100):
        # Set a random pen color
        r = random.random()
        g = random.random()
        b = random.random()
        turtle.pencolor(r, g, b)
        
        # Draw a rectangle of a certain size
        draw_rectangle(turtle, size)

        # Move the turtle to a new position
        turtle.right(5)
        size += 5

# Draw a spiral of rectangles
draw_spiral(my_turtle, size=5)

# Hide the turtle
my_turtle.hideturtle()

# This will stop the screen from being closed until the user closes it
turtle.done()
