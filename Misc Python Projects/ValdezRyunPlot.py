###########################################################################
#                              Plot Area                                  #
#                                                                         #
#   Programmed by Ryun Valdez 2/26/2015                                   #
#   Class:  CS301                                                         #
#   Instructor:  Dean Zeller                                              #
#                                                                         #
#   Description:  This file contains an graphic object and features to    #
#                 draw and plot functions, along with the corresponding   #
#                 labels, dots, and axis ranges.                          #
#                                                                         #
#   List of Features:                                                     #
#   The following features were added to the program after the template   #
#   was distributed:                                                      #
#       1. Cosmetic updates were added, graph is now presented inside     #
#          of a window with grid lines                                    #
#       2. Added a gui interface with slider bars to modify window        #
#       3. Added Riemann sum functionality for all types of               #
#          approximations                                                 #
#                                                                         #
#   Copyright:                                                            #
#   Code written based on a template written by Dean Zeller.              #
#   This file and all code within is copyright (c) 2015 Dean Zeller and   #
#   Ryun Valdez.  Permission to use for educational purposes only.        #
###########################################################################

from tkinter import *

class PlotArea:

    #######################################################################
    #  __init__ constructor                                               #
    #                                                                     #
    #  Initializes all attributes to given parameters.                    #
    #  Parameters:                                                        #
    #           canvas           Canvas to draw the function plot         #
    #           originX,originY  The origin of the coordinates            #
    #           xgridwidth       Number of pixels in a single unit        #
    #######################################################################
    def __init__ (self, canvas, originX=200,originY=300,
                  xgridwidth=20, ygridheight=20):
        self.c = canvas
        self.originX = originX
        self.originY = originY
        self.xgridwidth = xgridwidth
        self.ygridheight = ygridheight
        self.sum = 0

    #######################################################################
    #  point2grid                                                         #
    #                                                                     #
    #  Given a point, calculate the x and y coordinates for the graphic   #
    #  window.                                                            #
    #######################################################################
    def point2grid(self,p):   # translates a point to a gridpoint
        xgrid = self.originX + self.xgridwidth*p[0]
        ygrid = self.originY - self.ygridheight*p[1]
        return (xgrid,ygrid)

    #######################################################################
    #  labelPoint                                                         #
    #                                                                     #
    #  Label point p with the specified label.  The offset represents the #
    #  location of the label relative to the point location.              #
    #######################################################################
    def labelPoint(self,p,label="",offset=(5,5)):
        new = self.point2grid(p)
        x = new[0]
        y = y = new[1]
        self.c.create_text(x+offset[0],y+offset[1],
                           text=label, justify=LEFT, anchor=NW)

    #######################################################################
    #  dotPoint                                                           #
    #                                                                     #
    #  Given a point p, label with a dot of the specified dotsize, fill   #
    #  color, and outline color.
    #######################################################################
    def dotPoint(self,p,dotsize=3,fill="red", outline="black"):
        new = self.point2grid(p)
        x = new[0]
        y = y = new[1]
        self.c.create_oval(x-dotsize,y-dotsize,x+dotsize,y+dotsize,
                             fill=fill,outline=outline)

    #######################################################################
    #  labelFunction                                                      #
    #                                                                     #
    #  Given a function f and a list of xvalues, put a label and a dot at #
    #  each point listed.                                                 #
    #######################################################################
    def labelFunction(self, f, xvalues):
        for x in xvalues:
            y = f(x)
            label = "("+str(round(x,1))+","+str(round(y,1))+")"
            self.labelPoint((x,f(x)),label=label)
            self.dotPoint((x,f(x)))

    def riemannSum(self, f, start, end, rSeg,sType='left'):
        width = ((end - start) / rSeg)
        rSum = 0.0
        rSum2 = 0.0
        if sType=='left':
            x = start
            while x < end:
                self.c.create_polygon(self.point2grid((x,0)),
                                      self.point2grid((x,f(x))),
                                      self.point2grid((x+width,f(x))),
                                      self.point2grid((x+width,0)),
                                      fill="Turquoise", outline='black')
                rSum += f(x) * width
                x += width
            return rSum
        elif sType=='right':
            x = start+width
            #brute fix, the rounding has been off, this ensures it loops the right amount
            while x < end+(width/2):
                self.c.create_polygon(self.point2grid((x,0)),
                                      self.point2grid((x,f(x))),
                                      self.point2grid((x-width,f(x))),
                                      self.point2grid((x-width,0)),
                                      fill="Yellow", outline='black')
                rSum += f(x) * width
                x += width
            return rSum
        elif sType=='middle':
            x = (start+start+width)/2
            w2 = width/2
            while x < end:
                self.c.create_polygon(self.point2grid((x-w2,0)),
                                      self.point2grid((x-w2,f(x))),
                                      self.point2grid((x+w2,f(x))),
                                      self.point2grid((x+w2,0)),
                                      fill="LimeGreen", outline='black')
                rSum += f(x) * width
                x += width
            return rSum
        elif sType=='trap':
            #draw
            x = start
            while x < (end+end-width)/2:
                self.c.create_polygon(self.point2grid((x,0)),
                                      self.point2grid((x,f(x))),
                                      self.point2grid((x+width,f(x+width))),
                                      self.point2grid((x+width,0)),
                                      fill="Violet", outline='black')
                x += width
            #left
            x = start
            while x < end:
                rSum += f(x) * width
                x += width
            #right
            x = start+width
            while x < end+(width/2):
                rSum2 += f(x) * width
                x += width
            #sum
            rSum_final= (rSum+rSum2)/2
            return rSum_final          
    
    #######################################################################
    #  plot                                                               #
    #                                                                     #
    #  Plot a function in the window system.                              #
    #                                                                     #
    #  Parameters:                                                        #
    #           f           function to plot                              #
    #           start,end   x-coordinates of where to start and end plot  #
    #           segments    number of line segments used to draw the      #
    #                       function                                      #
    #           dotEvery    place a dot regularly on the function plot    #
    #                       (0 means no dots)                             #
    #           labelEvery  place a label regularly on the function plot  #
    #                       (0 means no labels)                           #
    #######################################################################
    def plot(self,f,start,end,segments=100,dotEvery=0,labelEvery=0,rSeg=6,
             sum_type='left',color="black"):   # plots a function for the given range
        #Draw Grid
        for i in range(int(500/self.ygridheight)+1): #hor-lines
            if self.originY+self.ygridheight*i <550:
                self.c.create_line(50, self.originY+self.ygridheight*i,
                                   550,self.originY+self.ygridheight*i)
            if self.originY+self.ygridheight*(i*-1)> 50:
                self.c.create_line(50, self.originY+self.ygridheight*(i*-1),
                                   550,self.originY+self.ygridheight*(i*-1))
        for i in range(int(500/self.xgridwidth)+1): #vert-lines
            if self.originX+self.xgridwidth*i <550:
                self.c.create_line(self.originX+self.xgridwidth*i, 50,
                                   self.originX+self.xgridwidth*i, 550)
            if self.originX+self.xgridwidth*(i*-1)> 50:
                self.c.create_line(self.originX+self.xgridwidth*(i*-1), 50,
                                   self.originX+self.xgridwidth*(i*-1), 550)
        self.sum = self.riemannSum(f,start,end, rSeg,sum_type) #Draw Riemann sum
        #Draw Function
        width = (end - start) / segments    # width of sections
        x = start
        y = f(x)
        prev = (x,y)   # must keep previous point to draw lines
        i = 0          # counter to draw dots and labels
        while x <= end:
            x += width
            y = f(x)
            new = (x,y)
            self.c.create_line(self.point2grid(prev),self.point2grid(new),
                               width=width,fill=color, tag='function')
            if dotEvery > 0 and i % dotEvery == 0:
                self.dotPoint(new,dotsize=3)
            if labelEvery > 0 and i % labelEvery == 0:
                label = "("+str(round(x,1))+","+str(round(y,1))+")"
                self.labelPoint(new,label=label)
            self.c.update()
            prev = new
            i += 1
        self.c.create_line(self.originX,25,self.originX,575,
                           width=3,arrow=BOTH)  # x-axis
        self.c.create_line(25,self.originY,575,self.originY,
                           width=3,arrow=BOTH)  # y-axis
        self.c.create_line(50,50, 50,550, 550,550, 550,50, 50,50, width=3)#Border
        self.c.create_text(150, 25, text="Riemann sum= "+str(self.sum),  #Riemann sum
                           width = 200, justify=CENTER)
