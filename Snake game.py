import turtle
import time
import random

delay = 0.1
Score = 0
High_Score = 0


w = turtle.Screen()
w.title("Snake Game")
w.bgcolor('white')
w.setup(width=600, height=600)
w.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"


food= turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("black")
food.penup()
food.goto(0,100)

segments = []

#score
s = turtle.Turtle()
s.speed(0)
s.shape("square")
s.color("black")
s.penup()
s.hideturtle()
s.goto(0,260)
s.write("Score: 0  High Score: 0", align = "center", font=("ds-digital", 24, "normal"))


def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

#keyboard
w.listen()
w.onkeypress(go_up, "w")
w.onkeypress(go_down, "s")
w.onkeypress(go_left, "a")
w.onkeypress(go_right, "d")

while True:
    w.update()

    
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        
        for segment in segments:
            segment.goto(1000,1000)
        
        segments.clear()
        Score = 0
        delay = 0.1

        s.clear()
        s.write("Score: {}  High Score: {}".format(Score, High_Score), align="center", font=("ds-digital", 24, "normal"))

    if head.distance(food) <20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment)
        
        delay -= 0.001
        Score += 10

        if Score > High_Score:
            High_Score = Score
        s.clear()
        s.write("Score: {}  High Score: {}".format(Score,High_Score), align="center", font=("ds-digital", 24, "normal")) 

    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            score = 0
            delay = 0.1
    
            s.clear()
            s.write("Score: {}  High Score: {}".format(Score,High_Score), align="center", font=("ds-digital", 24, "normal"))
    time.sleep(delay)
wn.mainloop()  
