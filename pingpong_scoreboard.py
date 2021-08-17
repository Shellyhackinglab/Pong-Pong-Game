from turtle import Turtle, Screen


ALIGN = "left"
FONT =("Courier",12,"normal")

class Howto1(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(0)
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-40,-100)   
        self.write(arg=f"\nL: press <-\nR: press ->",align=ALIGN,font=FONT)
    
class Howto2(Howto1):

    def __init__(self):
        super().__init__()
        self.goto(-40,100)
        self.write(arg=f"\nL: press a \nR: press s",align=ALIGN,font=FONT)


class Scoreboard1(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(0)
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-260,-20)   

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}",align=ALIGN,font=FONT)  
       # ↑self.bar.writeではない！
       #前は ---> self.write(arg=f"Score: {self.score}",move=False,align="center",font=("Arial",18,"normal"))  
       #のように書いていたけれど、ハードコーディングは好ましくないので、グローバル変数として外で定義しよう。
        
    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    

class Scoreboard2(Scoreboard1):

    def __init__(self):
        super().__init__()
        self.goto(-260,20)
    
    def update_scoreboard(self):
        super().update_scoreboard()

    def add_score(self):
        pass   
