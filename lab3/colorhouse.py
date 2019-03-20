from turtle import *
import turtle as t
import math
t.setup(800,800)
'''
You are to use functions and turtle graphics to draw the colored house
shown in the lab3 document. Choice of colors is up to you. Have fun.
'''
def drawoutline(t):
    '''
    This function draws the outline of a house using turtle t.
    '''
    ### Draw the rectangluar face of the house
    t.fillcolor('pink')
    t.begin_fill()
    t.forward(200)               ### <---- Your code goes there
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(400)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(200)
    t.end_fill()
    ### Draw the roof
    t.penup()     ### <---- Your code goes there    
    t.goto(200,150)
    t.left(120)
    t.pendown()
    t.fillcolor('brown')
    t.begin_fill()
    t.forward(150)
    t.left(60)
    t.forward(250)
    t.left(60)
    t.forward(150)
    t.end_fill()
 
def drawwindow(x, y, side,t,color):
    ''' 
    Draws a square window of length side with upper-left corner at 
    the point (x, y) using turtle t.
    '''
    t.penup()                     ### these lines move the turtle to the
    t.goto(x, y)              ### point (x, y) and orient the turtle             
    t.setheading(0) 
    t.fillcolor('white')                          ## to face East
    t.pendown()    
    t.begin_fill()
    ### Enter code to draw the sides of a window using a for-loop
    for count in range(4):
        t.forward(side)
        t.right(90)
    t.end_fill() 
    
def drawdoor(x,y,side,t,color):
    t.penup()                     ### these lines move the turtle to the
    t.goto(x, y)              ### point (x, y) and orient the turtle             
    t.setheading(0) 
    t.fillcolor('grey')                          ## to face East
    t.pendown()    
    t.begin_fill()
    for count in range(4):
        t.forward(side)
        t.right(90)
    t.end_fill()

def drawchimney(x,y,side,t,color):
    t.penup()
    t.goto(x,y)
    t.setheading(0)
    t.pendown()
    t.fillcolor('darkgrey')
    t.begin_fill()
    for count in range(4):
        t.forward(side)
        t.right(90)
    t.end_fill()
    
def drawdoorknob(x, y, radius, t,color):
    '''
    Draws a circular doorknob of radius r using turtle t.
    '''
    
    t.penup()                      ### these lines move the turtle to the
    t.goto(x, y - radius)                   ### point (x, y) and orient the turtle
    t.setheading(0)                ### to face East
    t.pendown()
    t.fillcolor('black')
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    ### Enter code to draw a circle for the doorknob
    
def drawmoon(x,y,radius,t,color):
    t.penup()
    t.goto(x,y-radius)
    t.setheading(0)
    t.pendown()
    t.fillcolor('darkgrey')               ### <---- Your code goes there
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def drawcrater(x,y,radius,t,color):
    t.penup()
    t.goto(x,y-radius)
    t.setheading(0)
    t.pendown()
    t.fillcolor('white')               ### <---- Your code goes there
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    
def drawwalk(t):
    '''
    This function draws the walkway with turtle t.
    '''
    ### Draw three lines to produce the walk.
    t.penup()
    t.goto(-55,0)
    t.pendown()
    t.goto(-95,-250)
    t.goto(95,-250)
    t.goto(55,0) 
    
def drawhouse(t):
    '''
    Draws a detailed house and moon using turtle t.
    '''
    drawoutline(t)                ### draw the house's outline
    
    drawwindow(110, 130, 50,t,color)  ### draw right window - each of these is a call to drawwindow()
    drawwindow(-160,130,50,t,color)      ### draw left window
    drawdoor(-50,105,100,t,color)      ### draw door
    drawchimney(70,320,40,t,color)          ### draw chimney    
    drawdoorknob(40,55,5,t,color)  ### draw the doorknob - each of these is a call to drawdoorknob()
    drawmoon(-300,350,70,t,color)      ### draw the moon
    drawcrater(-270,320,10,t,color)      ### draw crater 1
    drawcrater(-290,300,5,t,color)      ### draw crater 2
    drawcrater(-310,330,7,t,color)      ### draw crater 3
    drawcrater(-350,320,8,t,color)      ### draw crater 4
    drawwalk(t)### draw the walkway
    
### main() starter code    
wn = Screen()
alex = Turtle()
drawhouse(alex)      ### draw it

alex.penup()
alex.goto(-300, -300)             ### move turtle off to the side
t.done()
input()
