from turtle import *
from random import randint
import time

speed(10)
penup()
goto(-140, 140)



for step in range(15):
    write(step)
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)
hideturtle()


style="Verdana",15,"bold"

text = Turtle()
text.penup()
text.goto(-160, 250)
text.pendown()
text.color("red")
text.hideturtle()
text.write("Turtles! On your Marks!",font=style)

ada = Turtle()
ada.color('red')
ada.shape('turtle')
ada.penup()
ada.goto(-160,100)
ada.right(360)
ada.pendown()

bob = Turtle()
bob.color('green')
bob.shape('turtle')
bob.penup()
bob.goto(-160, 70)
bob.backward(50)
bob.forward(50)
bob.backward(50)
bob.forward(50)
bob.pendown()

greta = Turtle()
greta.color('purple')
greta.shape('turtle')
greta.penup()
greta.goto(-160, 40)
greta.backward(50)
greta.forward(50)
greta.backward(50)
greta.forward(50)
greta.pendown()


text.clear()
text.write("Turtles Get Set", font=style)

# pause computer for x number of millisecons
time.sleep(3)
text.clear()
text.write("GO!!!", font=style)

# loop 100 times
for turn in range(100):
    #move each turtle forward by a random number between 1 and 5
    ada.forward(randint(1,5))
    bob.forward(randint(1,5))
    greta.forward(randint(1,5))
