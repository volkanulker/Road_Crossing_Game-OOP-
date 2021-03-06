from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier",24,'normal')
GAME_OVER_FONT = ("Courier",48,'normal')

class LevelSign(Turtle):

    def __init__(self):
        self.level = 0
        super().__init__()
        self.refresh_score()
       
        
    def refresh_score(self ):
        self.level += 1
        self.reset()
        self.hideturtle()
        self.color('black')
        self.penup()
        self.goto(-200,250)
        self.write(f"Level: {self.level} " , False , ALIGNMENT, FONT)
    
    def game_over(self):
        self.goto( 0 , 0 )
        self.color('red')
        self.write("GAME OVER", align=ALIGNMENT,font=GAME_OVER_FONT)
        self.penup()
        self.goto(0 , -60)
        self.color('black')
        self.write("Click Screen To Exit", align=ALIGNMENT,font=FONT)

        