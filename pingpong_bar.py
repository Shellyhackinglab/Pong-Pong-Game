from turtle import Turtle, Screen

#BAR = Turtle(shape = "square")  #default square size = 20×20  BARとした方がいいのかself.barとした方がいいの
GAME_IS_ON = True
X1 = -260
Y1 = -260
X2 = -260
Y2 = 260
LEFT = 180
RIGHT = 0

class Bar1:
    
    def __init__(self):
        self.new_bar = []
        self.bar = Turtle(shape = "square")
        self.bar.speed(0)
        self.screen = Screen
        self.create_bar()   #ここでcreate_bar()を呼んでいるので、main.pyの方でcreate_bar()を呼ばなくて良い！
        self.bar.setpos(X1,Y1)

    def create_bar(self):
        #x = -260
        #y = -260
        self.bar.penup()
        self.bar.color("white","white")
        for i in range(0,3):
            self.new_bar.append(i)
            length = len(self.new_bar)
        #print(length)
        self.bar.turtlesize(stretch_wid=0.5,stretch_len=length,outline=1)  #barの大きさ長くする
    
    def move(self):
        self.bar.penup()
        for i in range(30):   #while GAME_IS_ON:
            if self.bar.xcor() > 260:
                self.bar.speed("fastest")   #端に行ったときにくるっと回転するのが見えなくなる
                self.bar.setheading(180)
            elif self.bar.xcor() < -260:
                self.bar.speed("fastest")
                self.bar.setheading(0)
            self.bar.speed(0)               #ここは0にしないと、回転している途中が現れるので方向キー押下するとあらぬ方向にいってしまうwww
            self.bar.forward(20)            #回転してる途中で左だの右だの追加で押すから変な挙動を示すのか。
                                            #speed(0)にしたらアニメーション消失するのでそういう現象もなくなったよ

    def right(self):
        self.bar.speed("fastest")   #speed(0)と同じ。端に行ったときにくるっと回転するのが見えなくなる
        self.bar.setheading(RIGHT)

    def left(self):
        self.bar.speed("fastest")   #speed(0)と同じ。端に行ったときにくるっと回転するのが見えなくなる
        self.bar.setheading(LEFT)
    
    def home(self):     #まだ使用していない
        GAME_IS_ON = False
        self.bar.home() 


class Bar2(Bar1):
    
    def __init__(self):
        super().__init__()
        self.bar.goto(X2,Y2)
    
    def create_bar(self):
        super().create_bar()
    
    def move(self):
        super().move()

    def right(self):
        super().right()

    def left(self):
        super().left()
