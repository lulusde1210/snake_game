from turtle import Turtle
SCORE_BOARD_POSITION = (0, 270)
FONT = ('Courier', 20, "normal")
ALIGNMENT = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(SCORE_BOARD_POSITION)
        self.update_score_board()
        self.ht()

    def update_score_board(self):
        self.clear()
        self.write(
            f"Score: {self.score} Highest Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_score_board()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", "w") as data:
            data.write(str(self.high_score))
        self.score = 0
        self.update_score_board()
