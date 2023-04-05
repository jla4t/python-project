from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.pu()
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 14, "normal"))

    def add_score(self):
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Arial", 14, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER.", align="center", font=("Arial", 48, "bold"))
        self.goto(0, -50)
        self.write(f"SCORE: {self.score}", align="center", font=("Arial", 48, "bold"))