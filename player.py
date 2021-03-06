from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.color('green')

    def move_up(self):
        self.setheading(90)
        self.goto(self.xcor(),self.ycor() + MOVE_DISTANCE)

    def move_down(self):
        self.setheading(270)
        if self.ycor() > -280:
            self.goto(self.xcor(),self.ycor() - MOVE_DISTANCE)

    def move_right(self):
        self.setheading(0)
        if self.xcor() < 270:
            self.goto(self.xcor() + MOVE_DISTANCE , self.ycor() )

    def move_left(self):
        self.setheading(180)
        if self.xcor() > -270:
            self.goto(self.xcor() - MOVE_DISTANCE , self.ycor() )


    def refresh_position(self):
        self.goto( STARTING_POSITION )
