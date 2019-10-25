# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random

#-----game configuration----
turtleshape = "turtle"
turtlesize = 2
turtlecolor = "purple"

score = 0

timer = 7
counter_interval = 1000   #1000 represents 1 second
timer_up = False


#-----initialize turtle-----
bill = trtl.Turtle(shape = turtleshape)
bill.color(turtlecolor)
bill.shapesize(turtlesize)
bill.speed(0)

score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(-460, 370)
score_writer.ht()

font_setup = ("Ariel" , 20, "bold")
score_writer.write(score, font=font_setup)

counter =  trtl.Turtle()
counter.ht()
counter.penup()
counter.goto(340,370)

#-----game functions--------
def turtle_clicked(x,y):
    print("bill got clicked")
    change_position()
    update_score()


def change_position():
    bill.penup()
    bill.ht()
    if not timer_up:
      billx = random.randint(-400,400)
      billy = random.randint(-300,300)
      bill.goto(billx, billy)
      bill.st()

def update_score():
    global score
    score += 1
    print(score)
    score_writer.clear()
    score_writer.write(score, font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 


#-----events----------------


wn = trtl.Screen()

wn.bgcolor("lightblue")
bill.onclick(turtle_clicked)
wn.ontimer(countdown, counter_interval) 
wn.mainloop()