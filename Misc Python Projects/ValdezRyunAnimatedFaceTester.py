###########################################################################
#                           "Jokes"                                       #
#                                                                         #
#  Programmed by Ryun Valdez                                              #
#                                                                         #
#                                                                         #
#  EXTERNAL FILES                                                         #
#  The following external files are used in the process of running the    #
#  animation.                                                             #
#       ZellerDeanAnimatedFace, written by Dean Zeller                    #
#           Face -- An animated smiley face                               #
#           Pose -- The available emotions for the face                   #
#                                                                         #
###########################################################################
from ZellerDeanAnimatedFace import Face
from ZellerDeanAnimatedFace import Pose
import random
from tkinter import *
c = Canvas(width=500, height=500, bg='white')
c.pack(expand=YES, fill=BOTH)

longDelay = 1000
mediumDelay = 250
shortDelay = 50

title = c.create_text(250,30, text="Jokes!",
                      font=("Helvetica",36))

Mark = Face(c, left=-100, top=200, width=100, height=100,
            faceColor="Wheat", eyeColor="white", pupilColor="SteelBlue",
            pose=Pose.GLAD)
Jesse = Face(c, left=500, top=200, width=100, height=100,
             faceColor="Tan", eyeColor="white",
             pose=Pose.HAPPY)
Mark.draw()
Jesse.draw()
c.after(mediumDelay)
c.update()
for i in range(10):
    Mark.move(20,0,delay=shortDelay)
    Jesse.move(-20,0,delay=shortDelay)
c.after(longDelay)
c.itemconfig(title, text="")
c.update()

c.after(mediumDelay)
Mark_text = c.create_text(150, 350, text="Mark", justify=CENTER)
c.update()

c.after(longDelay)
Jesse_text = c.create_text(350, 350, text="Jesse", width = 200, justify=CENTER)
c.update()

c.after(longDelay)
c.itemconfig(Mark_text, text="")
c.itemconfig(Jesse_text, text="")
c.update()

c.after(longDelay)
c.itemconfig(Jesse_text,text="Hey Mark!")
c.update()

c.after(longDelay)
c.itemconfig(Jesse_text, text="Do you want to hear a joke?")
c.update()

c.after(1500)
c.itemconfig(Mark_text, text="Sure")
c.update()

c.after(longDelay)
c.itemconfig(Mark_text, text="")
c.itemconfig(Jesse_text, text="Ok!")
c.update()

c.after(1500)
c.itemconfig(Jesse_text,text="Yo' Mama so stupid,")
c.update()
c.after(1500)
c.itemconfig(Jesse_text,text="....she payed 100 Grand for the candy bar!")
c.update()
Mark.setPose(Pose.ANXIOUS, delay=1500)

c.after(longDelay)
Jesse.setPose(Pose.ECSTATIC, delay=0)
c.itemconfig(Jesse_text,text="HAH!")
c.update()
Jesse.setPose(Pose.HAPPY, delay=mediumDelay)

c.after(longDelay)
c.itemconfig(Jesse_text, text="Ok!")
c.update()

c.after(longDelay)
c.itemconfig(Jesse_text, text="Another one!")
c.update()

c.after(1500)
c.itemconfig(Jesse_text, text="Yo' Mama so ugly,")
c.update()
c.after(1500)
c.itemconfig(Jesse_text,text="....the only thing she turns on is the TV!")
c.update()
c.after(2000)
Mark.setProperties(faceColor="IndianRed")
c.update()

c.after(longDelay)
Jesse.setPose(Pose.ECSTATIC, delay=0)
c.itemconfig(Jesse_text,font=("Times", 24),text="HAH!")
c.update()
Jesse.setPose(Pose.HAPPY, delay=mediumDelay)

c.after(longDelay)
c.itemconfig(Jesse_text, font=("Helvetica", 12), text="One more!")
c.update()

c.after(1500)
c.itemconfig(Jesse_text, text="Yo' Mama is so fat,")
c.update()
c.after(1500)
c.itemconfig(Jesse_text,text="....when she goes to the beach, the whales start singing, we are family!")
c.update()
Mark.scale(1.5,1.5, delay=3000)
c.update()

Jesse.move(50,0,delay=longDelay)
c.itemconfig(Jesse_text, text="")
Jesse_text = c.create_text(400, 350, text="Too far?", width = 200, justify=CENTER)
c.update()

c.after(longDelay)
c.itemconfig(Jesse_text, text="Ok,")
c.update()

c.after(2000)
c.itemconfig(Jesse_text, text="...Yo' Mama has more crabs than Red Lobster.")
c.update()
c.after(2000)
Mark.setProperties(eyeColor="Red", pupilColor="Black")
c.update()

c.after(longDelay)
for i in range(10):
    Jesse.scale(.9, .9, delay=shortDelay)
c.itemconfig(Jesse_text, text="")
c.update()

c.itemconfig(Mark_text, font=("Times", 24), text="Fuck off, mate")
c.update()

c.after(longDelay)
for i in range(20):
    Jesse.move(20, 0, delay=25)
Jesse.delete(0)

c.itemconfig(Mark_text, text="")

Mark.delete(longDelay)

c.after(longDelay)
c.create_text(250,250, text="The End!",font=("Helvetica",36))
c.update()


