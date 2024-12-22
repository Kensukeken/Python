import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("lightgreen")
screen.title("Happy 20th Birthday :3")
screen.setup(width=800, height=570)

# Create a turtle instance
t = turtle.Turtle()
t.speed(2)  # Set the turtle speed
t.pensize(3)

def draw_cake():
    # Define the color for the cake base
    snow_colors = ["green"]

    # Function to draw a line
    def line(x1, y1, x2, y2, color, width):
        t.penup()
        t.goto(x1, y1)
        t.pendown()
        t.color(color)
        t.pensize(width)
        t.goto(x2, y2)
        t.penup()

    # Draw the cake base
    line(-190, -180, 190, -180, random.choice(snow_colors), 6)
    
    # Draw the bottom layer of the cake (Chocolate Brown)
    t.penup()
    t.goto(-100, -150)
    t.pendown()
    t.color("#3E2723")
    t.begin_fill()
    for _ in range(2):
        t.forward(200)
        t.left(90)
        t.forward(100)
        t.left(90)
    t.end_fill()

    # Draw the middle layer of the cake (Light Brown)
    t.penup()
    t.goto(-80, -50)
    t.pendown()
    t.color("#8D6E63")
    t.begin_fill()
    for _ in range(2):
        t.forward(160)
        t.left(90)
        t.forward(70)
        t.left(90)
    t.end_fill()

    # Draw the top layer of the cake (Creamy Light Brown)
    t.penup()
    t.goto(-60, 20)
    t.pendown()
    t.color("#D7CCC8")
    t.begin_fill()
    for _ in range(2):
        t.forward(120)
        t.left(90)
        t.forward(50)
        t.left(90)
    t.end_fill()

    # Draw the candles on the top layer
    t.penup()
    t.goto(-50, 70)
    t.color("white")
    for _ in range(4):
        t.pendown()
        t.begin_fill()
        t.forward(10)
        t.left(90)
        t.forward(30)
        t.left(90)
        t.forward(10)
        t.left(90)
        t.forward(30)
        t.left(90)
        t.end_fill()
        t.penup()
        t.forward(30)

# Function to write text part by part
def write_text_part_by_part():
    t.penup()
    t.color("darkblue")

    # Write "Happy"
    t.goto(-150, 200)
    for char in "Happy":
        t.write(char, align="center", font=("Times New Roman", 24, "bold"))
        t.goto(t.xcor() + 30, t.ycor())

    # Write "20th"
    t.goto(20, 200)
    for char in "20th":
        t.write(char, align="center", font=("Times New Roman", 24, "bold"))
        t.goto(t.xcor() + 30, t.ycor())

    # Write "Birthday"
    t.goto(-150, 160)
    for char in "Birthday":
        t.write(char, align="center", font=("Times New Roman", 24, "bold"))
        t.goto(t.xcor() + 30, t.ycor())

    # Write ":3"
    t.goto(90, 160)
    for char in ":3":
        t.write(char, align="center", font=("Times New Roman", 24, "bold"))
        t.goto(t.xcor() + 30, t.ycor())

# Function to draw a heart
def draw_heart(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("red")
    t.begin_fill()

    # Set starting orientation for the heart
    t.setheading(0)

    # Draw a smoother heart with symmetrical curves
    t.left(50)
    t.forward(60)
    t.circle(30, 200)
    t.right(120)
    t.circle(30, 200)
    t.forward(60)

    t.end_fill()
    t.setheading(0)  # Reset heading to 0 after drawing the heart

# Function to draw stars
def draw_stars():
    t.penup()
    t.color("yellow")
    positions = [(-250, 250), (-280, 200), (200, 250), (250, 200)]

    for pos in positions:
        t.goto(pos)
        t.pendown()
        t.begin_fill()
        for _ in range(5):  # Draw a 5-pointed star
            t.forward(40)
            t.right(144)
        t.end_fill()
        t.penup()

# Draw the text part by part
write_text_part_by_part()

# Draw the cake below the text
draw_cake()

# Draw the stars
draw_stars()

# Draw the heart at the specified position
draw_heart(190, -120)

# Hide the turtle and display the result
t.hideturtle()
screen.mainloop()
