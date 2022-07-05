from turtle import Turtle, Screen

tim = Turtle()


def forward():
    tim.forward(10)


def backward():
    tim.backward(10)


def right():
    tim.right(10)


def left():
    tim.left(10)


screen = Screen()

screen.onkey(forward, "Up")
screen.onkey(backward, "Down")
screen.onkey(right, "Right")
screen.onkey(left, "Left")

screen.listen()

screen.exitonclick()
