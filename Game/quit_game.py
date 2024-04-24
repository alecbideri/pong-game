from turtle import Turtle

align = "center"
font = ("Courier", 12, "normal")

class QuitGame(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 0)  # Position the text in the center of the screen

    def display_game_over(self):
        self.write("GAME OVER", align=align, font=font)

