from turtle import Turtle

ALIGNMENT="center"
FONT = ('Courier', 20, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.speed("fastest")
        self.goto(0, 260)
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER :(", move=False, align=ALIGNMENT, font=FONT)




