################################################################################
##                          Function Plot                                     ##
##                                                                            ##
##              Programmed by Ryun Valdez                                     ##
##              Class: CS301                                                  ##
##              Instructor: Dean Zeller                                       ##
##                                                                            ##
##              Description: This is an animation of a Function Plot          ##
##                             Using Lightsabers!                             ##
##                                                                            ##
################################################################################

from tkinter import *
c = Canvas(width=600, height=600, bg='white')
c.pack(expand=YES, fill=BOTH)

def drawLine(x,y,x2,y2,color, width):
    for i in range(1,61):
        c.after(8)
        c.create_line(x,y, x-(i*((x-x2)/60)),y-(i*((y-y2)/60)),width = width,
                      fill=color)
        c.update()



#Lightsaber Hilts
#Red
for i in range(1,61):
    c.after(16)
    c.create_polygon(95-(180-3*i),450, 110-(180-3*i),470,
                     70-(180-3*i),490, 55-(180-3*i),470, fill="wheat")
    c.update()
c.create_polygon(95,450, 110,470, 70,490, 55,470, fill="grey")

#Green
for i in range(1,61):
    c.after(16)
    c.create_polygon(410+(180-3*i),505, 430+(180-3*i),495,
                     460+(180-3*i),525, 440+(180-3*i),525, fill="wheat")
    c.update()
c.create_polygon(410,505, 430,495,460,525, 440,535, fill="grey")

#Draw y = 1/2x+1
#(0,1)(10,6)
drawLine(100,460, 500,260, "red", 6)

#Draw y = -x+8
#(0,8)(8,0)
drawLine(420,500, 100,180, "green", 6)

#Reset Canvas (not really, painting over it actually)
c.after(500)
c.create_rectangle(0,0, 600,600, fill="white")
c.create_line(100,180, 420,500, width=3, fill="green")
c.create_line(100,460, 500,260, width=3, fill="red")
c.update()

#Draw Y-Axis
drawLine(100,500, 100,100, "black", 3)
c.create_text(100,90,text="Y", width=20,fill='black',font=("Helvetica",12)
              ,justify=CENTER, anchor=CENTER)

#Draw X-Axis
drawLine(100,500, 500,500, "black", 3)
c.create_text(510,500,text="X", width=20,fill='black',font=("Helvetica",12)
              ,justify=CENTER, anchor=CENTER)

#Draw Columns
for i in range(1,10):
    c.after(50)
    x = i*(400/10)
    c.create_line(x+100,100, x+100, 500)
    c.update()

#Draw Rows
for i in range(1,10):
    c.after(50)
    y = i*(400/10)
    c.create_line(100,y+100, 500, y+100)
    c.update()

#Draw Axis Numbers
for i in range(1,4):
    c.after(100)
    x = i*(400/10)
    c.create_text(100+x,520,text=i, width=20,fill='black',
              font=("Helvetica",12),justify=CENTER, anchor=N)
    c.update()
for i in range(1,4):
    c.after(100)
    y = i*(400/10)
    c.create_text(80,500-y,text=i, width=20,fill='black',
              font=("Helvetica",12),justify=LEFT, anchor=E)
    c.update()
#Draw Function Labels
c.after(500)
c.create_text(510,100,text="y = -x+8 ", width=200,fill='green',
              font=("Helvetica",12),justify=RIGHT, anchor=W)
c.update()
c.after(500)
c.create_text(510,125,text="y = 1/2x+1", width=200,fill='red',
              font=("Helvetica",12),justify=RIGHT, anchor=W)
c.update()

#Draw Title
title = c.create_text(-100,25,text="Lightsaber Line Functions", width=600,
                  fill='black',font=("Helvetica",24),justify=LEFT, anchor=N)
for i in range(1,61):
    c.after(16)
    c.move(title, 400/60, 0)
    c.update()






