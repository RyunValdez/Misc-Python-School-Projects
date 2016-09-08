###########################################################################
#                              Plot Area Tester                           #
#                                                                         #
#   Programmed by Ryun Valdez  2/26/2015                                  #
#   Class:  CS301                                                         #
#   Instructor:  Dean Zeller                                              #
#                                                                         #
#   Description:  This file is a functionality and interface test for the #
#                 PlotArea object.                                        #
#                                                                         #
#   Copyright:                                                            #
#   This file and all code within is copyright (c) 2015 Dean Zeller and   #
#   Ryun Valdez.  Permission to use for educational purposes only.        #
###########################################################################
from tkinter import *
from ValdezRyunPlot import PlotArea
import math

running = True
Gui = Tk()
Gui.geometry('900x600+100+100')

c = Canvas(width=600,height=600,bg='white')
c.grid(row=0, column=0, rowspan=25)

def function1(x):
    return -x*x+4
def function2(x):
    return math.cos(5*x)+x
def function3(x):
    return (5*x**3-6*x)/(x**2+2)

f1_integral= 10.667
f2_integral=-0.21761
f3_integral=0
    
#relative = answer/actual

functions = [function1,function2,function3]
integrals = [f1_integral,f2_integral,f3_integral]
sum_types = ['left','right','middle','trap']

p = PlotArea(c, originX=300, originY=300,xgridwidth=50,ygridheight=50)
p.labelPoint((0,0),label="Origin",offset=(5,5))
p.dotPoint((0,0),dotsize=5,fill='green')
p.plot(functions[0],-2,2)
p.labelFunction(functions[0],[-2,-1,0,1,2])
c.create_text(400, 25, text="Actual sum= "+str(integrals[0]),#Actual sum
                           width = 200, justify=CENTER)
c.create_text(425, 575, text="Error= "+str(integrals[0]-p.sum),     #Error
                           width = 200, justify=CENTER)
c.create_text(150, 575, text="Relative error= "+str(p.sum/integrals[0]),#Relative error
                           width = 200, justify=CENTER)

Label(Gui, font=("Helvetica", 24), text="Reimann Sums").grid(row=0,column=2,columnspan=6)

#Radio Buttons
func_var = IntVar()
sum_var = IntVar()

Label(Gui, font=("Helvetica", 12), text="Functions:").grid(row=1,column=2,sticky=W, padx=6)
f1_button = Radiobutton(Gui, text="-x*x+4", variable=func_var, value=0)
f1_button.grid(row=2, column=2, sticky=W, padx=10)
f1_button.select()
f2_button = Radiobutton(Gui, text="cos(5x)+x", variable=func_var, value=1)
f2_button.grid(row=2,column=3, sticky=W, padx=10)
f3_button = Radiobutton(Gui, text="(5x^3-6x)/(x^2+2)", wraplength=55, variable=func_var, value=2)
f3_button.grid(row=2,column=4, sticky=W, padx=10)

Label(Gui, font=("Helvetica", 12), text="Sum Types:").grid(row=3,column=2,sticky=W, padx=6)
leftSum_button = Radiobutton(Gui, text="Left", variable=sum_var, value=0)
leftSum_button.grid(row=4, column=2, sticky=W, padx=10)
leftSum_button.select()
rightSum_button = Radiobutton(Gui, text="Right", variable=sum_var, value=1)
rightSum_button.grid(row=5, column=2, sticky=W, padx=10)
middleSum_button = Radiobutton(Gui, text="Middle", variable=sum_var, value=2)
middleSum_button.grid(row=4, column=3, sticky=W, padx=10)
trapSum_button = Radiobutton(Gui, text="Trapezoid", variable=sum_var, value=3)
trapSum_button.grid(row=5, column=3, sticky=W, padx=10)

#Scales
r_scale = Scale(Gui, from_=1, to=100, label='Riemann Sum Intervals', orient=HORIZONTAL)
r_scale.grid(row=6, column=2, columnspan=3, sticky=W+E, padx=10)
r_scale.set(6)

ygrid_scale = Scale(Gui, from_=100, to=10, label='Y Grid Height')
ygrid_scale.grid(row=7, column=2, columnspan=2, sticky=W)
ygrid_scale.set(50)

xgrid_scale = Scale(Gui, from_=10, to=100, label='X Grid Width',orient=HORIZONTAL)
xgrid_scale.grid(row=7, column=3, columnspan=2, sticky=W+E, padx=10)
xgrid_scale.set(50)

originY_scale = Scale(Gui, from_=-250, to=250, label='Y Origin Point')
originY_scale.grid(row=9, column=2, columnspan=2,sticky=W)
originY_scale.set(0)

originX_scale = Scale(Gui, from_=-250, to=250, label='X Origin Point', orient=HORIZONTAL)
originX_scale.grid(row=9, column=3, columnspan=2,sticky=W+E, padx=10)
originX_scale.set(0)

#Update Button clears and re-plots
def update():
    c.delete('all')
    global func_var
    global sum_var
    n = func_var.get()
    s = sum_var.get()
    p = PlotArea(c, originX=originX_scale.get()+300, originY=originY_scale.get()+300,
                 xgridwidth=xgrid_scale.get(),ygridheight=ygrid_scale.get())
    p.labelPoint((0,0),label="Origin",offset=(5,5))
    p.dotPoint((0,0),dotsize=5,fill='green')
    p.plot(functions[n],-2,2,rSeg=r_scale.get(),sum_type=sum_types[s])
    p.labelFunction(functions[n],[-2,-1,0,1,2])
    c.create_text(400, 25, text="Actual sum= "+str(integrals[n]),
                       width = 200, justify=CENTER)
    c.create_text(425, 575, text="Error= "+str(integrals[n]-p.sum),     #Error
                           width = 200, justify=CENTER)
    c.create_text(150, 575, text="Relative error= "+str(p.sum/integrals[n]),#Relative error
                           width = 200, justify=CENTER)
    c.update()
update_button = Button(Gui, text="UPDATE", command=update, bg='LimeGreen')
update_button.grid(row=10, column=2, rowspan=12, columnspan=3, sticky=N+S+W+E, padx=30)

