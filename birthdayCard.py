from turtle import Turtle, Screen

t = Turtle()
s = Screen()
s.setup(500,700)
s.bgcolor('misty rose')
name = input('Please enter your name')   
t.color('pink')
t.write('Happy Birthday',  font=('Forte', 35, 'normal'), align="center") 
t.up()
t.sety(-60)
t.down()
t.write(name, font=('Gabriola', 40, 'normal'), align="center") 
t.color('magenta')
t.hideturtle()

t.speed(0) 

#Draw top row of stars
t.up()
t.goto(-250,90)
t.down()
for i in range(15):
    # 1 star
    t.up()
    t.setx(t.xcor()+30)
    t.down()
    for j in range(5):
        t.forward(30)
        t.right(144)
#Draw bottom row of stars
t.up()
t.goto(-250,-90)
t.down()
for i in range(15):
    # 1 star
    t.up()
    t.setx(t.xcor()+30)
    t.down()
    for j in range(5):
        t.forward(30)
        t.right(144)
       
#Draw left side of stars    
t.up()
t.goto(-250,120)
t.down()
for i in range(7):
    # 1 star
    t.up()
    t.sety(t.ycor()-30)
    t.down()
    for j in range(5):
        t.forward(30)
        t.right(144)    

#draw right side of stars   
t.up()
t.goto(200,90)
t.down()
for i in range(5):
    # 1 star
    t.up()
    t.sety(t.ycor()-30)
    t.down()
    for j in range(5):
        t.forward(30)
        t.right(144)      

#candle green with flame 
t.up()
t.goto(10,100)
t.down()
t.begin_fill()
t.color('light green')
t.goto(10,200)
t.setheading(180)
t.forward(20)
t.setheading(270)
t.forward(100)
t.end_fill() 

t.up()
t.setheading(90)
t.forward(110)
t.setheading(0)
t.forward(9)
t.down()
t.begin_fill()
t.color('light green')
t.circle(7)
t.end_fill()
    
#candle blue with flame 
t.up()
t.goto(60,100)
t.down()
t.begin_fill()
t.color('deep sky blue')
t.goto(60,200)
t.setheading(180)
t.forward(20)
t.setheading(270)
t.forward(100)
t.end_fill() 

t.up()
t.setheading(90)
t.forward(110)
t.setheading(0)
t.forward(9)
t.down()
t.begin_fill()
t.color('deep sky blue')
t.circle(7)
t.end_fill()

#candle plum with flame 
t.up()
t.goto(110,100)
t.down()
t.begin_fill()
t.color('plum ')
t.goto(110,200)
t.setheading(180)
t.forward(20)
t.setheading(270)
t.forward(100)
t.end_fill() 

t.up()
t.setheading(90)
t.forward(110)
t.setheading(0)
t.forward(9)
t.down()
t.begin_fill()
t.color('plum')
t.circle(7)
t.end_fill()


##candle yellow  with flame 
t.up()
t.goto(-40,100)
t.down()
t.begin_fill()
t.color(' yellow')
t.goto(-40,200)
t.setheading(180)
t.forward(20)
t.setheading(270)
t.forward(100)
t.end_fill() 

t.up()
t.setheading(90)
t.forward(110)
t.setheading(0)
t.forward(9)
t.down()
t.begin_fill()
t.color('yellow')
t.circle(7)
t.end_fill()

##candle orange  with flame  
t.up()
t.goto(-90,100)
t.down()
t.begin_fill()
t.color(' orange')
t.goto(-90,200)
t.setheading(180)
t.forward(20)
t.setheading(270)
t.forward(100)
t.end_fill()

t.up()
t.setheading(90)
t.forward(110)
t.setheading(0)
t.forward(9)
t.down()
t.begin_fill()
t.color('orange')
t.circle(7)
t.end_fill()

#candle red with flame  
t.up()
t.goto(-140,100)
t.down()
t.begin_fill()
t.color(' red')
t.goto(-140,200)
t.setheading(180)
t.forward(20)
t.setheading(270)
t.forward(100)
t.end_fill()       
    
t.up()
t.setheading(90)
t.forward(110)
t.setheading(0)
t.forward(9)
t.down()
t.begin_fill()
t.color('red')
t.circle(7)
t.end_fill()

#candle pink with flame   
t.up()
t.goto(160,100)
t.down()
t.begin_fill()
t.color('hot pink')
t.goto(160,200)
t.setheading(180)
t.forward(20)
t.setheading(270)
t.forward(100)
t.end_fill() 

t.up()
t.setheading(90)
t.forward(110)
t.setheading(0)
t.forward(9)
t.down()
t.begin_fill()
t.color('hot pink')
t.circle(7)
t.end_fill()
    
    
    
    
    
