from turtle import Turtle
SCORE_BOARD_POSITION = (0, 270)
FONT = ('Arial', 20, "normal")
ALIGNMENT = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(SCORE_BOARD_POSITION)
        self.update_score_board()
        self.ht()

    def update_score_board(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_score_board()

    def game_over(self):
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
