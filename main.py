from turtle import Turtle,Screen
import random

is_race_on = False

screen = Screen()

screen.setup(height=400,width=500)
user_bet = screen.textinput("Make your bet","Which turtle will win the race? Enter a color")
print(user_bet)
colors =["red","green","orange","blue","yellow","purple"]
all_turtles =[]

#Turtles object creation
# Turtle co-ordinate
x_pos=-230
y_pos = -100

#Create 6 turtle
for i in range(6):
    object_name = (f"tim{i}")
    object_name= Turtle(shape="turtle")
    object_name.penup()
    object_name.color(colors[i])
    object_name.goto(x= x_pos, y =-y_pos)
    y_pos = y_pos + 40
    all_turtles.append(object_name)

#Game Logic creation
if user_bet:
    is_race_on =True

while is_race_on:
    for turtle in all_turtles:
        # 230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        # Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)





screen.exitonclick()
