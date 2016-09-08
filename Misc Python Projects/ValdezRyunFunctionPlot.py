################################################################################
##                          Function Plot                                     ##
##                                                                            ##
##              Programmed by Ryun Valdez                                     ##
##              Class: CS301                                                  ##
##              Instructor: Dean Zeller                                       ##
##                                                                            ##
##              Description: This is a drawing of a Function Plot             ##
##                                                                            ##
################################################################################

from tkinter import *
c = Canvas(width=600, height=600, bg='white')
c.pack(expand=YES, fill=BOTH)

#Draw Y-Axis
c.create_line(100,100, 100, 500, width=3)
c.create_text(100,90,text="Y", width=20,fill='black',font=("Helvetica",12)
              ,justify=CENTER, anchor=CENTER)

#Draw X-Axis
c.create_line(100,500, 500, 500, width=3)
c.create_text(510,500,text="X", width=20,fill='black',font=("Helvetica",12)
              ,justify=CENTER, anchor=CENTER)

#Draw Columns
for i in range(1,10):
    x = i*(400/10)
    c.create_line(x+100,100, x+100, 500)

#Draw Rows
for i in range(1,10):
    y = i*(400/10)
    c.create_line(100,y+100, 500, y+100)

#Draw y = -x+8
#(0,8)(8,0)
c.create_line(100,180, 420,500, width=3, fill="green")
c.create_text(420,510,text="y = -x+8 ", width=200,fill='green',
              font=("Helvetica",12),justify=CENTER, anchor=N)

#Draw y = 1/2x+1
#(0,1)(10,6)
c.create_line(100,460, 500,260, width=3, fill="red")
c.create_text(510,260,text="y = 1/2x+1", width=200,fill='red',
              font=("Helvetica",12),justify=RIGHT, anchor=W)

#Draw Axis Numbers
for i in range(1,4):
    x = i*(400/10)
    c.create_text(100+x,510,text=i, width=20,fill='black',
              font=("Helvetica",12),justify=CENTER, anchor=N)
for i in range(0,4):
    y = i*(400/10)
    c.create_text(90,500-y,text=i, width=20,fill='black',
              font=("Helvetica",12),justify=LEFT, anchor=E)

#Draw Title
c.create_text(300,25,text="Random Line Functions", width=600,fill='black',font=("Helvetica",24)
              ,justify=LEFT, anchor=N)






