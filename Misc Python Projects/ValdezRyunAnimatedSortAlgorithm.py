################################################################################
##                          Sorting Algorithms                                ##
##                                                                            ##
#   Programmed by Ryun Valdez  3/13/2015                                      ##
#   Class:  CS301                                                             ##
#   Instructor:  Dean Zeller                                                  ##
#                                                                             ##
#   Description:  This file is a gui application to visually show             ##
#                 searching algorithms                                        ##
#                                                                             ##
##  Credit to Dean Zeller for class outline                                   ##
##                                                                            ##
################################################################################
from tkinter import *

Gui = Tk()
Gui.geometry('700x500+25+150')

c = Canvas(width=500, height=500, bg='white')
c.grid(row=0, column=0, rowspan=25)

#Globals..eesh
sortList = [5,0,8,3,4,7,9,1,2,6]
sortedList = [0,1,2,3,4,5,6,7,8,9]
comps = 0
swaps = 0

color = ['red','orangered','orange','yellow','lime',
          'limegreen','dodgerblue','cyan','magenta','purple']

#Color Bars to visually represent the list
class colorBar:

    objectName = "Bar"
    objectNum = 0
    
    def __init__(self, canvas, left=0,top=0,
                 width=10, height=400,color=color[0], number=0):
        self.c = canvas
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.color = color
        self.number = number
        ########
        self.tag = colorBar.objectName + str(colorBar.objectNum)
        colorBar.objectNum += 1
        self.right = self.left + self.width
        self.bottom = self.top + self.height
        self.center = (self.left + self.right) / 2.0
        self.middle = (self.top + self.bottom) / 2.0
    def draw(self):
        self.c.create_rectangle(self.left,self.top,
                                self.right,
                                self.bottom,
                                fill=self.color, tag=self.tag)
        self.c.create_text(self.center, self.middle,font=("Times", 24),
                           text=str(self.number),justify=CENTER, tag=self.tag)
#Functions        
def drawArray(array):
    colorBar.objectNum = 0
    for i in range(0,len(array)):
        colorBar.draw(colorBar(c, left=i*50, top=1,
                               width=50, height = 450,
                               color=color[array[i]], number=array[i]))
def swap(array, i, j):
    global swaps
    if i!=j:
        swaps += 1
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
    return array

def insertionSort(array):
    global comps
    for i in range(1, len(array)):
        current = array[i]
        j = i
        c.after(250)
        c.delete("pointer","pointer2","pointer3")
        c.create_polygon(15+i*50,480, 25+i*50,470, 35+i*50,480,
                         tag="pointer")
        c.update()
        c.after(250)
        c.move("Bar"+str(i),0,-150)
        c.update()
        while j > 0 and array[j-1] > current:
            comps+=1
            c.after(250)
            c.delete("pointer2")
            #Left
            c.create_polygon(-5+(j-1)*50,480, 5+(j-1)*50,475, -5+(j-1)*50,470,
                         tag="pointer2",fill="black")
            #Right
            c.create_polygon(15+(j-1)*50,480, 5+(j-1)*50,475, 15+(j-1)*50,470,
                         tag="pointer2",fill="black")
            c.update()
            array[j] = array[j-1]
            j = j - 1
            c.after(250)
            c.move("Bar"+str(j),50,0)
            c.update()
        array[j] = current
        c.after(250)
        #Left
        c.create_polygon(-5+j*50,480, 5+j*50,475, -5+j*50,470,
                     tag="pointer3",fill="green")
        #Right
        c.create_polygon(15+j*50,480, 5+j*50,475, 15+j*50,470,
                     tag="pointer3",fill="green")
        c.update()
        
        c.after(500)
        c.delete(ALL)
        drawArray(array)
        c.update()
    c.delete("pointer","pointer2","pointer3")

def selectionSort(array):
    global comps
    for i in range(len(array)):
        minimum = i
        c.after(250)
        c.delete("pointer3")
        c.create_polygon(15+i*50,480, 25+i*50,470, 35+i*50,480,
                         tag="pointer")
        c.update()
        for j in range(i+1, len(array)):
            comps += 1
            c.after(250)
            c.delete("pointer2")
            c.create_polygon(15+j*50,480, 25+j*50,470, 35+j*50,480,
                             tag="pointer2", fill='red')
            c.update()
            if array[j] < array[minimum]:
                c.after(250)
                c.delete("pointer3")
                c.create_polygon(15+j*50,480, 25+j*50,470, 35+j*50,480,
                             tag="pointer3", fill='green')
                c.update()
                minimum = j
        swap(array,minimum,i)
        c.after(500)
        drawArray(array)
        c.delete("pointer","pointer2")
        c.update()
        
#Quick Sort#       
def quickSort(array):
    requickSort(array, 0, len(array)-1)
    c.delete("pointer")
    c.update()
    return array

def requickSort(array, low, high):
    if low < high:
        wall = partition(array,low,high)
        requickSort(array, low, wall-1)
        requickSort(array, wall, high)

def partition(array, low, high):
    global comps
    pivot = high
    c.after(250)
    c.delete("pointer")
    c.create_polygon(15+pivot*50,480, 25+pivot*50,470, 35+pivot*50,480,
                         tag="pointer")
    c.update()
    for i in range(low,high):
        comps+=1
        if array[i] <= array[pivot]:
            swap(array, i, low)
            low+=1
            c.after(250)
            drawArray(sortList)
            c.update()
    c.after(250)
    swap(array,low,high)
    c.update()
    return low
#End Quick Sort#


#Draw
drawArray(sortList)

#Radio Buttons#
sort_var = IntVar()

#Arrays
Label(Gui, font=("Helvetica", 12), text="Sorts:").grid(row=1,column=2,sticky=W, padx=6)
a1_button = Radiobutton(Gui, text="Insertion Sort", variable=sort_var, value=0)
a1_button.grid(row=2, column=2, sticky=W, padx=10)
a1_button.select()
a2_button = Radiobutton(Gui, text="Selection Sort", variable=sort_var, value=1)
a2_button.grid(row=3,column=2, sticky=W, padx=10)
a3_button = Radiobutton(Gui, text="Quick Sort", variable=sort_var, value=2)
a3_button.grid(row=4,column=2, sticky=W, padx=10)
compLabel = Label(Gui, font=("Helvetica", 12), text="Comparisons: "+str(comps))
compLabel.grid(row=6,column=2,sticky=W, padx=6)
swapLabel= Label(Gui, font=("Helvetica", 12), text="Swaps: "+str(swaps))
swapLabel.grid(row=7,column=2,sticky=W, padx=6)
####

#Animate!
def animate():
    global comps
    global swaps
    comps = 0
    swaps = 0
    compLabel.config(text="Comparisons: "+str(comps))
    swapLabel.config(text="Swaps: "+str(swaps))
    if sort_var.get()==0:
        insertionSort(sortList)
    if sort_var.get()==1:
        selectionSort(sortList)
    if sort_var.get()==2:
        quickSort(sortList)
    compLabel.config(text="Comparisons: "+str(comps))
    swapLabel.config(text="Swaps: "+str(swaps))
            
update_button = Button(Gui, text="ANIMATE!", command=animate, bg='LimeGreen')
update_button.grid(row=16, column=2, rowspan=6, columnspan=2, sticky=N+W+S+E, padx=10)
#Reset
def reset():
    global sortList
    global comps
    global swaps
    comps = 0
    swaps = 0
    compLabel.config(text="Comparisons: "+str(comps))
    swapLabel.config(text="Swaps: "+str(swaps))
    c.delete(ALL)
    sortList = [5,0,8,3,4,7,9,1,2,6]
    drawArray(sortList)
    
update_button = Button(Gui, text="Reset", command=reset, bg='Red')
update_button.grid(row=16, column=3, rowspan=6, columnspan=2, sticky=N+W+S+E, padx=10)
