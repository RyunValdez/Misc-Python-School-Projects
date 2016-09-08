################################################################################
##                          Sudoku Table Animation                            ##
##                                                                            ##
##              Programmed by Ryun Valdez                                     ##
##              Class: CS301                                                  ##
##              Instructor: Dean Zeller                                       ##
##                                                                            ##
##              Description: This is an animated Sudoku puzzle                ##
##                                                                            ##
################################################################################

from tkinter import *
c = Canvas(width=700, height=700, bg='white')
c.pack(expand=YES, fill=BOTH)

##Function insertNum##(int,int,str)
def insertNum(x, y, n):
    x = 50+((600/9)/2+(x*600/9))
    y = 50+((600/9)/2+(y*600/9))
    c.create_text(x,y,text=n, width=50,fill='black',font=("Helvetica",24)
                  ,justify=LEFT, anchor=CENTER)
def insertBox(x,y):
    x = 50+(x*600/9)
    y = 50+(y*600/9)
    c.create_rectangle(x,y, x+600/9,y+600/9, width=1)
    
##End Function insertNum##

insertBox(0,0)
insertBox(0,1)
#Draw Table Frame
c.create_rectangle(50,50, 650,650, width=3)

#Draw Title
c.create_text(350,10,text="SUDOKU", width=600,fill='black',font=("Helvetica",24)
              ,justify=LEFT, anchor=N)

#Draw Thick Columns
c.create_line(250,50, 250, 650, width=3)
c.create_line(450,50, 450, 650, width=3)

#Draw Columns
for i in range(1,9):
    x = i*(600/9)
    c.create_line(x+50,50, x+50, 650)
    
#Draw Thick Rows
c.create_line(50,250, 650, 250, width=3)
c.create_line(50,450, 650, 450, width=3)

#Draw Rows
for i in range(1,9):
    y = i*(600/9)
    c.create_line(50,y+50, 650, y+50)

#Draw Numbers
insertNum(0,0,"1")
insertNum(2,0,"7")
insertNum(3,0,"4")
insertNum(4,0,"8")
insertNum(8,0,"9")
insertNum(4,1,"1")
insertNum(0,2,"3")
insertNum(1,2,"8")
insertNum(7,2,"1")
insertNum(1,3,"1")
insertNum(5,3,"8")
insertNum(8,3,"3")
insertNum(1,4,"6")
insertNum(7,4,"2")
insertNum(0,5,"4")
insertNum(3,5,"2")
insertNum(7,5,"7")
insertNum(1,6,"5")
insertNum(7,6,"6")
insertNum(8,6,"1")
insertNum(4,7,"9")
insertNum(8,7,"7")
insertNum(0,8,"9")
insertNum(4,8,"1")
insertNum(5,8,"2")
insertNum(6,8,"5")
