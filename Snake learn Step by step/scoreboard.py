from turtle import Turtle

ALIGNMENT = "center"
FONT = ("monospace", 20, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_num = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=250)
        self.scored_fun()

    def scored_fun(self):

        self.score_text = self.write(arg=f"Score: {self.score_num}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font= FONT)

    def increase_score(self):
        self.score_num += 1
        self.clear()
        self.scored_fun()