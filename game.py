#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 22:52:52 2021

@author: jelhar
"""

import turtle
import time
import random as rd

BLOCK_SIZE = 60
BORDER = 13
STAMP_SIZE = 20  # Defualt value used to get pixel-level control of turtle size
ROWS = 8
COLUMNS = 8
SPEED = 10

sc=turtle.Screen()
sc.title("choques")
sc.bgcolor("gray")
WIDTH = COLUMNS * (BLOCK_SIZE + BORDER)
HEIGHT = ROWS * (BLOCK_SIZE + BORDER)
sc.setup(WIDTH, HEIGHT)
sc.setworldcoordinates(0, sc.window_height(), sc.window_width(), 0)
sc.tracer(0)

fld=turtle.Turtle()
fld.shape("square")
fld.color("orange")
fld.shapesize(BLOCK_SIZE / STAMP_SIZE)
fld.penup()

for col_num in range(COLUMNS):
    fld.goto((BLOCK_SIZE // 2) + col_num * (BLOCK_SIZE + BORDER),
                     (BLOCK_SIZE // 2) + 0* (BLOCK_SIZE + BORDER))
    fld.stamp()

for row_num in range(ROWS):
    fld.goto((BLOCK_SIZE // 2) + col_num * (BLOCK_SIZE + BORDER),
                     (BLOCK_SIZE // 2) + row_num* (BLOCK_SIZE + BORDER))
    fld.stamp()
    
for row_num in range(ROWS):
    fld.goto((BLOCK_SIZE // 2) + 0 * (BLOCK_SIZE + BORDER),
                     (BLOCK_SIZE // 2) + row_num* (BLOCK_SIZE + BORDER))
    fld.stamp()
    
for col_num in range(COLUMNS):
    fld.goto((BLOCK_SIZE // 2) + col_num * (BLOCK_SIZE + BORDER),
                     (BLOCK_SIZE // 2) + row_num* (BLOCK_SIZE + BORDER))
    fld.stamp()

#My turtle enemy
en1 = turtle.Turtle() 
en1 .speed(1.5) 
en1 .shape("turtle")
en1 .shapesize(BLOCK_SIZE / STAMP_SIZE) 
en1 .color("red") 
en1 .penup() 
en1 .goto((((BLOCK_SIZE // 2) + col_num * (BLOCK_SIZE + BORDER))*(3/4)),
                     ((BLOCK_SIZE // 2) + row_num* (BLOCK_SIZE + BORDER))*(3/4))
"""
en.stamp()
"""
en2 = turtle.Turtle() 
en2 .speed(1.5) 
en2 .shape("turtle")
en2 .shapesize(BLOCK_SIZE / STAMP_SIZE) 
en2 .color("red") 
en2 .penup() 
en2 .goto((((BLOCK_SIZE // 2) + col_num * (BLOCK_SIZE + BORDER))*(1/4)),
                     ((BLOCK_SIZE // 2) + row_num* (BLOCK_SIZE + BORDER))*(1/4))
"""
en.stamp()
en .goto(((BLOCK_SIZE // 2) + col_num * (BLOCK_SIZE + BORDER)),
                     ((BLOCK_SIZE // 2) + row_num* (BLOCK_SIZE + BORDER))*(1/4))
en.stamp()
"""

en3 = turtle.Turtle() 
en3 .speed(1.5) 
en3 .shape("turtle")
en3 .shapesize(BLOCK_SIZE / STAMP_SIZE) 
en3 .color("red") 
en3 .penup() 
en3 .goto((((BLOCK_SIZE // 2) + col_num * (BLOCK_SIZE + BORDER))*(1/4)),
                     ((BLOCK_SIZE // 2) + row_num* (BLOCK_SIZE + BORDER))*(3/4))

en4 = turtle.Turtle() 
en4 .speed(1.5) 
en4 .shape("turtle")
en4 .shapesize(BLOCK_SIZE / STAMP_SIZE) 
en4 .color("red") 
en4 .penup() 
en4 .goto((((BLOCK_SIZE // 2) + col_num * (BLOCK_SIZE + BORDER))*(3/4)),
                     ((BLOCK_SIZE // 2) + row_num* (BLOCK_SIZE + BORDER))*(1/4))


# My turtle shape 
turt = turtle.Turtle() 
turt .speed(40) 
turt .shape("turtle")
turt .shapesize(BLOCK_SIZE / STAMP_SIZE) 
turt .color("blue") 
turt .penup() 
turt .goto(((BLOCK_SIZE // 2) + col_num * (BLOCK_SIZE + BORDER))/2,
                     ((BLOCK_SIZE // 2) + row_num* (BLOCK_SIZE + BORDER))/2)

#parametros de medicion
arrib=((BLOCK_SIZE // 2) + (1)* (BLOCK_SIZE + BORDER))
abaj=((BLOCK_SIZE // 2) + row_num* (BLOCK_SIZE + BORDER))
derr=((BLOCK_SIZE // 2) + col_num * (BLOCK_SIZE + BORDER))
izq=((BLOCK_SIZE // 2) + 1* (BLOCK_SIZE + BORDER))


#Scoreboards
bds=turtle.Turtle()
bds.speed(0)
bds.shape("square")
bds.color("black")
bds.penup()
bds.hideturtle()
bds.goto((BLOCK_SIZE // 2) + 5 * (BLOCK_SIZE + BORDER),
                     (BLOCK_SIZE // 2) + 0* (BLOCK_SIZE + BORDER))
bds.write("Score:0 ",align="center",font=("Arial", 24, "bold"))
h =0

# Food turtle
food= turtle.Turtle() 
food.speed(0)
food.shape("circle")
food.color("black")
food.penup()
    #random inicio
    
a=rd.uniform((arrib+(0.1)*BLOCK_SIZE),(abaj-BLOCK_SIZE))
b=rd.uniform((izq-STAMP_SIZE),(derr-(3.8)*STAMP_SIZE))
food.goto(a, b)

sc.tracer(1)



# Functions to move paddle vertically
def bajar():
	y = turt .ycor()
	y += 20
	turt .sety(y)


def subir():
	y = turt .ycor()
	y -= 20
	turt .sety(y)

def right():
	x = turt .xcor()
	x += 20
	turt .setx(x)


def left():
	x = turt .xcor()
	x -= 20
	turt .setx(x)
    
# Keyboard bindings
sc.listen()
sc.onkeypress(subir,"w")
sc.onkeypress(bajar, "s")
sc.onkeypress(right,"d")
sc.onkeypress(left, "a")

def mov_en1():
    angle=rd.randint(0,90)
    dist=rd.randint(25,100)
    en1.left(angle)
    en1.forward(dist)
    if en1 .ycor()> (abaj-BLOCK_SIZE):
        en1 .sety(abaj-BLOCK_SIZE)
        
    if en1 .ycor()< (arrib+(0.1)*BLOCK_SIZE):
        en1 .sety(arrib+(0.1)*BLOCK_SIZE)
    
    if en1 .xcor()> (derr-(3.8)*STAMP_SIZE):
        en1 .setx(derr-(3.8)*STAMP_SIZE)
        
    if en1 .xcor()< (izq-STAMP_SIZE):
        en1 .setx(izq-STAMP_SIZE)
def mov_en2():
    angle=rd.randint(0,90)
    dist=rd.randint(25,100)
    en2.right(angle)
    en2.forward(dist)
    if en2 .ycor()> (abaj-BLOCK_SIZE):
        en2 .sety(abaj-BLOCK_SIZE)
        
    if en2 .ycor()< (arrib+(0.1)*BLOCK_SIZE):
        en2 .sety(arrib+(0.1)*BLOCK_SIZE)
    
    if en2 .xcor()> (derr-(3.8)*STAMP_SIZE):
        en2 .setx(derr-(3.8)*STAMP_SIZE)
        
    if en2 .xcor()< (izq-STAMP_SIZE):
        en2 .setx(izq-STAMP_SIZE)
def mov_en3():
    angle=rd.randint(0,90)
    dist=rd.randint(25,100)
    en3.right(angle)
    en3.forward(dist)
    if en3 .ycor()> (abaj-BLOCK_SIZE):
        en3 .sety(abaj-BLOCK_SIZE)
        
    if en3 .ycor()< (arrib+(0.1)*BLOCK_SIZE):
        en3 .sety(arrib+(0.1)*BLOCK_SIZE)
    
    if en3 .xcor()> (derr-(3.8)*STAMP_SIZE):
        en3 .setx(derr-(3.8)*STAMP_SIZE)
        
    if en3 .xcor()< (izq-STAMP_SIZE):
        en3 .setx(izq-STAMP_SIZE)
        
def mov_en4():
    angle=rd.randint(0,90)
    dist=rd.randint(25,100)
    en4.right(angle)
    en4.forward(dist)
    if en4 .ycor()> (abaj-BLOCK_SIZE):
        en4 .sety(abaj-BLOCK_SIZE)
        
    if en4 .ycor()< (arrib+(0.1)*BLOCK_SIZE):
        en4 .sety(arrib+(0.1)*BLOCK_SIZE)
    
    if en4 .xcor()> (derr-(3.8)*STAMP_SIZE):
        en4 .setx(derr-(3.8)*STAMP_SIZE)
        
    if en4 .xcor()< (izq-STAMP_SIZE):
        en4 .setx(izq-STAMP_SIZE)
    
pause= False
game = True
# Main game loop
while game == True:
    sc.update()
    
    # Checking borders    
    if turt .ycor()> (abaj-BLOCK_SIZE):
        turt .sety(abaj-BLOCK_SIZE)
        
    if turt .ycor()< (arrib+(0.1)*BLOCK_SIZE):
        turt .sety(arrib+(0.1)*BLOCK_SIZE)
    
    if turt .xcor()> (derr-(3.8)*STAMP_SIZE):
        turt .setx(derr-(3.8)*STAMP_SIZE)
        
    if turt .xcor()< (izq-STAMP_SIZE):
        turt .setx(izq-STAMP_SIZE)
        
    mov_en1()
    mov_en2()
    mov_en3()
    mov_en4()
    
    #food collision
    if (turt.distance(food)<30):
        a=rd.uniform((arrib+(0.1)*BLOCK_SIZE),(abaj-BLOCK_SIZE))
        b=rd.uniform((izq-STAMP_SIZE),(derr-(3.8)*STAMP_SIZE))
        food.penup()
        food.goto(a, b)
        h +=10
        bds.clear()
        bds.write("Score: {} ".format(h),align="center",font=("Arial", 24, "bold"))
    
    # Paddle ball collision
    if (turt.distance(en1)<60 or turt.distance(en2)<60 or turt.distance(en3)<60 or turt.distance(en4)<60):
        pause= True
        
        gmvr=turtle.Turtle()
        gmvr.speed(0)
        gmvr.shape("square")
        gmvr.color("purple")
        gmvr.penup()
        gmvr.goto((BLOCK_SIZE // 2) + (3.6) * (BLOCK_SIZE + BORDER),
                             (BLOCK_SIZE // 2) + 5* (BLOCK_SIZE + BORDER))
        gmvr.write(" GAME OVER ",align="center",font=("Arial", 48, "bold"))
        
        while pause== True :
            time.sleep(5)
        
sc.mainloop()