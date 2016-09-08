################################################################################
##                          Searching Algorithms                              ##
##                                                                            ##
#   Programmed by Ryun Valdez  3/6/2015                                       ##
#   Class:  CS301                                                             ##
#   Instructor:  Dean Zeller                                                  ##
#                                                                             ##
#   Description:  This file is a gui application to visually show             ##
#                 searching algorithms                                        ##
#                                                                             ##
##                                                                            ##
################################################################################
from tkinter import *

Gui = Tk()
Gui.geometry('700x500+25+150')

c = Canvas(width=500, height=500, bg='white')
c.grid(row=0, column=0, rowspan=25)

unorderedList = [5,4,8,3,0,7,9,1,2]
unevenList = [1,2,4,7,8,9,15,17,18]
orderedList = [1,2,3,4,5,6,7,8,9]
firstRun = True

c.create_text(250, 100, font=("Times", 36),
                         text="Search Algorithms!",justify=CENTER, tag="top")

#Number Boxes to visually represent the list
class numBox:

    objectName = "Box"
    objectNum = 0
    
    def __init__(self, canvas, left=0,top=0,size=100,
                 number=1, color="yellow", textColor="black"):
        self.c = canvas
        self.left = left
        self.top = top
        self.size = size
        self.number = number
        self.color = color
        self.textColor = textColor
        ########
        self.tag = numBox.objectName + str(numBox.objectNum)
        numBox.objectNum += 1
        self.right = self.left + self.size
        self.bottom = self.top + self.size
        self.center = (self.left + self.right) / 2.0
        self.middle = (self.top + self.bottom) / 2.0
        self.textSize = int((self.size) / 2)
    def draw(self):
        self.c.create_rectangle(self.left,self.top,
                                self.left+self.size,
                                self.top+self.size,
                                fill=self.color, tag=self.tag)
        self.c.create_text(self.center, self.middle,font=("Times", self.textSize),
                           text=str(self.number),justify=CENTER, tag=self.tag)
#Draw a series of boxes based on the list        
def drawArray(array):
    numBox.objectNum = 0
    for i in range(0,len(array)):
        numBox.draw(numBox(c, 25+i*50, 225, size=50, number=array[i]))   

def linearSearch(array, target):
    c.delete(ALL)
    drawArray(array)
    c.create_text(250, 400, font=("Times", 36),
                  text="Searching for: "+str(target),
                  justify=CENTER)
    #Check every list item and ask if it is the target
    for i in range(0,len(array)):
        c.after(500)
        c.create_polygon(40+i*50,300, 50+i*50,290, 60+i*50,300, tag="pointer")
        c.update()
        #If it was found push it up
        if array[i] == target:
            c.itemconfig("pointer",fill="green")
            for j in range(10):
                c.after(50)
                c.move("Box"+str(i),0,-5)
                c.move("pointer",0,-5)
                c.update()
            return c.create_text(250, 100, font=("Times", 36),
                                 text="Found at: " +str(i+1),justify=CENTER)
        c.after(500)
        c.delete("pointer")
        c.update()
    #If it was never found, return not found
    return c.create_text(250, 100, font=("Times", 36),
                         text="Not Found :(",justify=CENTER)

def binarySearch(array, target, bottom, top):   #Recursive
    #Only draw list on first run
    global firstRun
    if firstRun == True:
        c.delete(ALL)
        drawArray(array)
        firstRun = False
    #Check to see if the list is a sorted list
    if sorted(array) != array:
        #If not return Error
        return c.create_text(250, 100, font=("Times", 36),
                         text="List not sorted :(",justify=CENTER)
    #Else declare target number       
    c.create_text(250, 400, font=("Times", 36),
                  text="Searching for: "+str(target),
                  justify=CENTER)
    if bottom <= top:
        #Find Mid animate pointer
        mid = int((top + bottom)/2)
        c.after(500)
        c.delete("pointer")
        c.create_polygon(40+mid*50,300, 50+mid*50,290, 60+mid*50,300,
                         tag="pointer", fill="black")
        c.update()
        #If mid is the answer, push it up
        if array[mid] == target:
            c.after(500)
            c.create_polygon(40+mid*50,300, 50+mid*50,290, 60+mid*50,300,
                         tag="pointer", fill="green")
            c.update()
            for j in range(10):
                c.after(50)
                c.move("Box"+str(mid),0,-5)
                c.move("pointer",0,-5)
                c.update()
            return c.create_text(250, 100, font=("Times", 36),
                                 text="Found at: " +str(mid+1),justify=CENTER)
        #Else if mid is below target it must be higher than expected,
        elif array[mid] < target:
            c.after(500)
            c.create_polygon(40+mid*50,300, 50+mid*50,290, 60+mid*50,300,
                         tag="pointer", fill="red")
            c.update()
            c.after(500)
            c.delete("pointer")
            #Left
            c.create_polygon(50+mid*50,310, 40+mid*50,300, 50+mid*50,290,
                         tag="pointer",fill="black")
            #Right
            c.create_polygon(50+mid*50,310, 60+mid*50,300, 50+mid*50,290,
                         tag="pointer",fill="black")
            c.update()
            c.after(500)
            c.create_polygon(50+mid*50,310, 40+mid*50,300, 50+mid*50,290,
                         tag="pointer",fill="Red")
            c.create_polygon(50+mid*50,310, 60+mid*50,300, 50+mid*50,290,
                         tag="pointer",fill="Green")
            c.update()
            return binarySearch(array, target, mid+1, top)
        #Or vice versa
        else:
            c.after(500)
            c.create_polygon(40+mid*50,300, 50+mid*50,290, 60+mid*50,300,
                         tag="pointer", fill="red")
            c.update()
            c.after(500)
            c.delete("pointer")
            #Left
            c.create_polygon(50+mid*50,310, 40+mid*50,300, 50+mid*50,290,
                         tag="pointer",fill="black")
            #Right
            c.create_polygon(50+mid*50,310, 60+mid*50,300, 50+mid*50,290,
                         tag="pointer",fill="black")
            c.update()
            c.after(500)
            c.create_polygon(50+mid*50,310, 40+mid*50,300, 50+mid*50,290,
                         tag="pointer",fill="Green")
            c.create_polygon(50+mid*50,310, 60+mid*50,300, 50+mid*50,290,
                         tag="pointer",fill="Red")
            c.update()
            return binarySearch(array, target, bottom, mid-1)
    #If it was never found send not found
    else:
        return c.create_text(250, 100, font=("Times", 36),
                         text="Not Found :(",justify=CENTER)

def interpolationSearch(array, target, bottom, top):
    #Deviation for first two items
    dev = (array[1]-array[0])
    #Only draw list on first run
    global firstRun
    if firstRun == True:
        c.delete(ALL)
        drawArray(array)
        firstRun = False
    #Determine if list is sorted
    if sorted(array) != array:
        #If not return Error
        return c.create_text(250, 100, font=("Times", 36),
                         text="List not sorted :(",justify=CENTER, tag="top")
    #Determine if the list is uniform
    for i in range(0,len(array)-1):
        if array[i]+dev!=array[i+1]:
            #if not, warn the user
            c.create_text(250, 100, font=("Times", 36),
                          text="List not optimal :(",justify=CENTER, tag="top")
    c.create_text(250, 400, font=("Times", 36),
                  text="Searching for: "+str(target),
                  justify=CENTER, tag = "bottom")
    if bottom <= top:
        #Determine the mid, place pointer
        size = top - bottom
        range_ = array[top] - array[bottom]
        mid = int(bottom + ((target-array[bottom])*size)/range_)
        c.after(500)
        c.delete("pointer")
        c.create_polygon(40+mid*50,300, 50+mid*50,290, 60+mid*50,300,
                         tag="pointer", fill="black")
        c.update()
        #If the mid is the answer(almost every time)push the answer up
        if array[mid] == target:
            c.after(500)
            c.create_polygon(40+mid*50,300, 50+mid*50,290, 60+mid*50,300,
                         tag="pointer", fill="green")
            c.update()
            for j in range(10):
                c.after(50)
                c.move("Box"+str(mid),0,-5)
                c.move("pointer",0,-5)
                c.update()
            c.delete("top")
            return c.create_text(250, 100, font=("Times", 36),
                                 text="Found at: " +str(mid+1),justify=CENTER)
        #Else if mid is less than the target, the target must be higher
        elif array[mid] < target:
            c.after(500)
            c.create_polygon(40+mid*50,300, 50+mid*50,290, 60+mid*50,300,
                         tag="pointer", fill="red")
            c.update()
            c.after(500)
            c.delete("pointer")
            #Left
            c.create_polygon(50+mid*50,310, 40+mid*50,300, 50+mid*50,290,
                         tag="pointer",fill="black")
            #Right
            c.create_polygon(50+mid*50,310, 60+mid*50,300, 50+mid*50,290,
                         tag="pointer",fill="black")
            c.update()
            c.after(500)
            c.create_polygon(50+mid*50,310, 40+mid*50,300, 50+mid*50,290,
                         tag="pointer",fill="Red")
            c.create_polygon(50+mid*50,310, 60+mid*50,300, 50+mid*50,290,
                         tag="pointer",fill="Green")
            c.update()
            return interpolationSearch(array, target, mid+1,top)
        #Or vice versa
        else:
            c.after(500)
            c.create_polygon(40+mid*50,300, 50+mid*50,290, 60+mid*50,300,
                         tag="pointer", fill="red")
            c.update()
            c.after(500)
            c.delete("pointer")
            #Left
            c.create_polygon(50+mid*50,310, 40+mid*50,300, 50+mid*50,290,
                         tag="pointer",fill="black")
            #Right
            c.create_polygon(50+mid*50,310, 60+mid*50,300, 50+mid*50,290,
                         tag="pointer",fill="black")
            c.update()
            c.after(500)
            c.create_polygon(50+mid*50,310, 40+mid*50,300, 50+mid*50,290,
                         tag="pointer",fill="Green")
            c.create_polygon(50+mid*50,310, 60+mid*50,300, 50+mid*50,290,
                         tag="pointer",fill="Red")
            c.update()
            return interpolationSearch(array, target, bottom, mid-1)
    #If the answer was never found, return not found
    else:
        c.delete("top")
        return c.create_text(250, 100, font=("Times", 36),
                         text="Not Found :(",justify=CENTER)

#Radio Buttons#
list_var = IntVar()
src_var = IntVar()

#Arrays
Label(Gui, font=("Helvetica", 12), text="Lists:").grid(row=1,column=2,sticky=W, padx=6)
a1_button = Radiobutton(Gui, text="[1,2,3,4,5,6,7,8,9]", variable=list_var, value=0)
a1_button.grid(row=2, column=2, sticky=W, padx=10)
a1_button.select()
a2_button = Radiobutton(Gui, text="[5,4,8,3,0,7,9,1,2]", variable=list_var, value=1)
a2_button.grid(row=3,column=2, sticky=W, padx=10)
a3_button = Radiobutton(Gui, text="[1,2,4,7,8,9,15,17,18]", variable=list_var, value=2)
a3_button.grid(row=4,column=2, sticky=W, padx=10)
#Searches
Label(Gui, font=("Helvetica", 12), text="Searches:").grid(row=5,column=2,sticky=W, padx=6)
s1_button = Radiobutton(Gui, text="Linear Search", variable=src_var, value=0)
s1_button.grid(row=6, column=2, sticky=W, padx=10)
s1_button.select()
s2_button = Radiobutton(Gui, text="Binary Search", variable=src_var, value=1)
s2_button.grid(row=7,column=2, sticky=W, padx=10)
s3_button = Radiobutton(Gui, text="Interpolation Search", wraplength=75, variable=src_var, value=2)
s3_button.grid(row=8,column=2, sticky=W, padx=10)
####

#Input
Label(Gui, font=("Helvetica", 12), text="Input Target Number:").grid(row=9,column=2,sticky=W, padx=6)
Input = Entry(Gui)
Input.grid(row=10, column=2, sticky=W, padx=10)

#Animate!
def update():
    if src_var.get()==0:
        if list_var.get()==0:
            linearSearch(orderedList, int(Input.get()))
        elif list_var.get()==1:
            linearSearch(unorderedList, int(Input.get()))
        else:
            linearSearch(unevenList, int(Input.get()))
    elif src_var.get()==1:
        if list_var.get()==0:
            binarySearch(orderedList, int(Input.get()), 0,8)
        elif list_var.get()==1:
            binarySearch(unorderedList, int(Input.get()), 0,8)
        else:
            binarySearch(unevenList, int(Input.get()), 0,8)
    else:
        if list_var.get()==0:
            interpolationSearch(orderedList, int(Input.get()), 0,8)
        elif list_var.get()==1:
            interpolationSearch(unorderedList, int(Input.get()), 0,8)
        else:
            interpolationSearch(unevenList, int(Input.get()), 0,8)
    global firstRun
    firstRun=True
            
update_button = Button(Gui, text="ANIMATE!", command=update, bg='LimeGreen')
update_button.grid(row=16, column=2, rowspan=6, columnspan=2, sticky=N+S+W+E, padx=10)
