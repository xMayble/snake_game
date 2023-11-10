from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

x_position = [0,-20,-40]


for position in x_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(x=position, y=0)












screen.exitonclick()