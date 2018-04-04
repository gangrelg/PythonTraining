import turtle


def main():
    #Canvas and Turtle
    myWorld = turtle.Screen()
    character = turtle.Turtle()
    character.speed(10)
    #Set coordinates area(world)
    myWorld.setworldcoordinates(-0.5, -0.5, 3.5, 4.5)

    #Horizontal movement lines
    for i in range(0, 5):
        character.up()
        character.goto(0, i)
        character.down()
        character.forward(3)

    #Vertical movement lines
    character.left(90)  #Reset character to desired position
    for i in range(0, 4):
        character.up()
        character.goto(i, 0)
        character.down()
        character.forward(4)


main()
turtle.exitonclick()