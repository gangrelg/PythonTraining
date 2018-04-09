#  Developed by Galo Mosquera as well as for the comments

import turtle


def main():
    # Canvas and Turtle
    my_world = turtle.Screen()
    character = turtle.Turtle()
    # Set coordinates area(world)
    my_world.setworldcoordinates(-0.5, -0.5, 3.5, 4.5)
    character.speed(0)  # 0 is the faster top limit speed for turtle

    # Horizontal movement lines
    for i in range(0, 5):
        character.up()  # Its like a pen, when up, it just stops drawing the line
        character.goto(0, i)  # It goes to the desired coordinate
        character.down()  # It puts the pen down, ready to draw the line
        character.forward(3)  # Draw the line depending on the parameter (length)

    # Vertical movement lines
    character.left(90)  # Reset character to desired position (angle)
    for i in range(0, 4):
        character.up()
        character.goto(i, 0)
        character.down()
        character.forward(4)

    for i in range(1):
            character.goto(2.35,2.99)
            character.write("*",font=('Arial', 70, 'normal'))


main()
turtle.exitonclick()