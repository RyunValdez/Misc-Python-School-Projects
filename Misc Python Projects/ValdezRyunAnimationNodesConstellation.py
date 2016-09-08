################################################################################
##                      Nodes Constellation Animation                         ##
##                                                                            ##
##              Programmed by Ryun Valdez                                     ##
##              Class: CS301                                                  ##
##              Instructor: Dean Zeller                                       ##
##                                                                            ##
##              Description: This is an animation of a constellation          ##
##                                                                            ##
################################################################################

from tkinter import *
c = Canvas(width=600, height=750, bg='black')
c.pack(expand=YES, fill=BOTH)
import random

##Functions & Classes##
#
class Star:
    def __init__(self, size, x, y):
        self.size = size
        self.x = x
        self.y = y
    def insert(self):
        c.create_oval(self.x-self.size/2,self.y-self.size/2, self.x+self.size-self.size/2,
                    self.y+self.size-self.size/2,fill="white",outline="white",
                      tag="star")
    def connect(self, s2):
        for i in range(1,61):
            c.after(8)
            c.create_line(self.x,self.y, self.x-(i*((self.x-s2.x)/60)),
                          self.y-(i*((self.y-s2.y)/60)), fill="white", tag="line")
            c.update()
#   
def insertBg(size, x, y):
    c.create_oval(x-size/2,y-size/2, x+size-size/2,y+size-size/2, fill="white",
                  outline="white", tag="bg")
##End Functions & Classes##

#Draw Random Background
for i in range(1,125):
    x=random.random()*600
    y=random.random()*750
    insertBg(random.random()*10, x, y)

#Create Stars (Constellation)
#Shoulders
s1 = Star(15, 150, 320)
s2 = Star(15, 350, 340)
#Belt
s3 = Star(10, 220, 540)
s4 = Star(10, 250, 530)
s5 = Star(10, 280, 520)
#Feet
s6 = Star(15, 150, 730)
s7 = Star(15, 350, 700)
#Head
s8 = Star(10, 270, 250)
#Bow
s9 = Star(10, 525, 150)
s10 = Star(10, 530, 250)
s11 = Star(10, 570, 330)
s12 = Star(10, 550, 460)
s13 = Star(10, 510, 480)
#Arm
s14 = Star(10, 160, 20)
s15 = Star(10, 90, 25)
s16 = Star(10, 30, 110)
s17 = Star(10, 30, 160)
s18 = Star(10, 90, 270)

#Insert Stars
s1.insert()
s2.insert()
s3.insert()
s4.insert()
s5.insert()
s6.insert()
s7.insert()
s8.insert()
s9.insert()
s10.insert()
s11.insert()
s12.insert()
s13.insert()
s14.insert()
s15.insert()
s16.insert()
s17.insert()
s18.insert()

c.create_rectangle(0,0, 1,1)
c.update()
c.after(5000)
c.update()

##Draw Lines##Order is rearrangeable##
s14.connect(s15)
s15.connect(s16)
s16.connect(s17)
s17.connect(s18)
s18.connect(s1)
s1.connect(s8)
s1.connect(s3)
s8.connect(s2)
s3.connect(s6)
s2.connect(s5)
s6.connect(s7)
s7.connect(s5)
s5.connect(s4)
s3.connect(s4)
s2.connect(s11)
s11.connect(s12)
s11.connect(s10)
s12.connect(s13)
s10.connect(s9)

##Highlight##
c.itemconfig("line", fill="Gold", width=2)
c.itemconfig("star", outline="Gold", width=2)
title = c.create_text(300,100,text="ORION", width=600,fill='Gold',
        font=("Helvetica",1),justify=CENTER, anchor=CENTER)
c.tag_raise("star")
c.update()

for i in range(1,48):
    c.after(50)
    c.itemconfig(title, font=("Helvetica",2+i))
    c.update()





