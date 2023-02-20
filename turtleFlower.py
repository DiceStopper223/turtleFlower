import turtle
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
t.speed(0)
color = ("yellow", "red" , "green", "blue", "light pink", "orange", "cyan")

for i in range(150):
    t.pencolor(color[i&6])
    t.circle(190-i/2, 90)
    t.lt(90)
    t.circle(190-i/3, 90)
    t.lt(60)
screen.exitonclick()
