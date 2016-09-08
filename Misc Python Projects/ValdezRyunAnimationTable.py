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
class Box:
    def __init__(self,x,y):
        self.x = 50+(x*600/9)
        self.y = 50+(y*600/9)
    def insertBox(self,x,y):
        c.create_rectangle(self.x,self.y, self.x+600/9,self.y+600/9, width=1)
    def animateBox(self, speed):
        c.create_rectangle(self.x,0, self.x+600/9,600/9, width=1, tag ="cBox")
        for i in range(1,61):
                c.after(speed)
                c.move("cBox",0,(self.y/60))
                c.update()
        c.dtag("cBox","cBox")
##End Function insertNum##

#Draw Boxes
for i in range(0,9):
    for j in range(0,9):
        Box(8-j,8-i).animateBox(2)
        #if 8-j== and 8-i== :
            
        
#Draw Table Frame
c.after(500)
c.create_rectangle(50,50, 650,650, width=3)
c.update()

#Draw Thick Columns
c.after(500)
c.create_line(250,50, 250, 650, width=3)
c.create_line(450,50, 450, 650, width=3)
c.update()
    
#Draw Thick Rows
c.after(500)
c.create_line(50,250, 650, 250, width=3)
c.create_line(50,450, 650, 450, width=3)
c.update()

#Draw Numbers
c.after(500)
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
c.update()

#Draw Title
c.after(500)
c.create_text(350,10,text="SUDOKU", width=600,fill='black',font=("Helvetica",24)
              ,justify=LEFT, anchor=N)
c.update()
