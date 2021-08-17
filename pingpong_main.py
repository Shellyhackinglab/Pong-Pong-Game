from turtle import Turtle, Screen
from pingpong_bar import Bar1, Bar2
#from invader_food import Food
from pingpong_scoreboard import Scoreboard1, Scoreboard2
import threading

screen = Screen()
screen.setup(600,600)
#screen.tracer(1,0.8)
screen.bgcolor("black")
screen.title("Invader Game")
line = Turtle()
line.speed(0)
line.hideturtle()
line.color("white")
line.write(arg="-"*120,align="center" )

bar1 = Bar1()
bar2 = Bar2()
#food = Food()
scoreboard1 = Scoreboard1()
scoreboard2 = Scoreboard2()
scoreboard1.update_scoreboard()
scoreboard2.update_scoreboard()

screen.listen()
screen.onkey(bar1.left, "Left")
screen.onkey(bar1.right, "Right")
screen.onkey(bar2.left, "a")
screen.onkey(bar2.right, "s")

#thread0 = threading.Thread(target=food.move)       #foodのスレッド
thread1 = threading.Thread(target=bar1.move)       #下：bar1, 上：bar2
#threading.Thread(target=target1,name=thread1)
thread2 = threading.Thread(target=bar2.move)
#threading.Thread(target=target2,name=thread2)
thread1.start()
thread2.start()
#thread0.start()

print(threading.active_count())  #---> スレッド数"4"になった！bar1, bar2, food, main

#.join()はこれ以降のメイン関数の処理を上記スレッドが終了するまで待機させるので、
#今回は不必要かなー。

screen.exitonclick()
