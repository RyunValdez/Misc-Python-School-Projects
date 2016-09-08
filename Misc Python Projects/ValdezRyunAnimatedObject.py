###########################################################################
#                              Animated Face                              #
#                                                                         #
#   Programmed by Dean Zeller (02-01-2015)                                #
#   Classes:  CG120, CS301                                                #
#   Instructor:  Dean Zeller                                              #
#                                                                         #
#   Description:  The file contains an animated graphic object and an     #
#                 accompanying enumerated data type to define the         #
#                 different poses.                                        #
#   Objects:                                                              #
#               Pose    Enumerated data type for nine different emotions. #
#               Face    A traditional smiley face with different faces    #
#                       (poses) for each emotion defined in the Emotions  #
#                       class.                                            #
#                                                                         #
#   Copyright:                                                            #
#       This file and all code within is copyright (c) 2015 Dean Zeller.  #
#   Permission to use for educational purposes only.                      #
###########################################################################
from tkinter import *

###########################################################################
#                           Pose                                          #
#                                                                         #
#   Description:  This class defines nine different emotions, for use     #
#                 in the Face class.  The emotions include:               #
#                 SAD, ANGRY, NEUTRAL, GLAD, HAPPY, SMIRK, ECSTATIC,      #
#                 DRUNK, and ANXIOUS.                                     #
#                                                                         #
###########################################################################

class Pose:  #enumerated data type
    SAD=0
    ANGRY=1
    NEUTRAL=2
    GLAD=3
    HAPPY=4
    SMIRK=5
    ECSTATIC=6
    DRUNK=7
    ANXIOUS=8
    numPoses=9   # number of poses, necessary for nextPose method

###########################################################################
#                                  Face                                   #
#                                                                         #
#   Description:  This uses the tkinter graphics library to create a      #
#                 classic smiley face, based on the user's parameters.    #
#                                                                         #
#   Parameters:                                                           #
#           canvas         Canvas to draw the picture                     #
#           left, top      Left and top of the entire picture             #
#           width, height  Width and height of the entire picture         #
#           faceColor      Color of the face                              #
#           eyeColor       Color of the eyes                              #
#           pupilColor     Color of the pupils                            #
#           pose           Emotion poses (see Pose class above)           #
#           name           Name of the face                               #
#           displayName    Boolean to display the character name          #
#                              0 -> does not display name                 #
#                              1 -> displays name                         #
#                                                                         #
###########################################################################
class Face:

    # class attributes
    objectName = "ZellerDeanAnimatedFace"  # Title for this object
    objectNum = 0                          # Number of instances created

    #######################################################################
    #  __init__ constructor                                               #
    #                                                                     #
    #  Initializes all attributes to given parameters.                    #
    #######################################################################
    def __init__ (self, canvas, left=0,top=0,width=100,height=100,
                  faceColor="yellow", eyeColor="white", pupilColor="black",
                  pose=Pose.HAPPY, name="blank", displayName=0):

    def draw(self):

        
    def move (self, deltaX=0, deltaY=0, delay=5):
        # adjust attributes
        self.left += deltaX
        self.top += deltaY
        self.right += deltaX
        self.bottom += deltaY
        self.center += deltaX
        self.middle += deltaY
        # move face
        self.c.after(delay)
        self.c.move(self.tag,deltaX,deltaY)
        self.c.update()

    #######################################################################
    #  moveTo method                                                      #
    #                                                                     #
    #  Moves the face on the canvas to a specific location, broken        #
    #  into a series of steps, each after the specified delay.            #
    #######################################################################
    def moveTo (self, x=0, y=0, steps=10, delay=5):
        # calculate deltaX and deltaY
        distX = x - self.left
        deltaX = distX * 1.0 / steps
        distY = y - self.top
        deltaY = distY * 1.0 / steps
        # move face in steps
        for i in range(steps):
            self.move(deltaX=deltaX, deltaY=deltaY, delay=delay)

    def setProperties (self, faceColor="default", eyeColor="default",
                       pupilColor="default"):

    #######################################################################
    #  setPose method                                                     #
    #                                                                     #
    #  Changes the pose of the face to the specified pose.                #
    #######################################################################
    def setPose (self, pose=Pose.HAPPY, delay=5):
        self.c.after(delay)
        self.delete(delay=0)
        self.pose = pose
        self.draw()
        self.c.update()

    #######################################################################
    #  nextPose method                                                    #
    #                                                                     #
    #  Changes the pose of the face to the next in the defined list.      #
    #######################################################################
    def nextPose (self, delay=5):
        self.c.after(delay)
        self.delete(delay=0)
        self.pose = (self.pose + 1) % Pose.numPoses
        self.draw()
        self.c.update()

    #######################################################################
    #  scale method                                                       #
    #                                                                     #
    #  Changes the size of the object, according to the xscale and        #
    #  yscale parameters, after a given delay.                            #
    #                                                                     #
    #  Note:  There is a bug in this method.  The left, right, top, and   #
    #  bottom are not recalculated.  For most cases, this will not affect #
    #  animation playback.  However, the potential for problems exist.    #
    #######################################################################
    def scale(self, xscale=1.0, yscale=1.0, delay=5):
        self.c.after(delay)
        self.c.scale(self.tag, self.center, self.middle, xscale, yscale)
        self.width = self.width * xscale
        self.height = self.height * yscale
        self.c.update()

    #######################################################################
    #  pause method                                                       #
    #                                                                     #
    #  Delays the animation, according to the after parameter specified.  #
    #######################################################################
    def pause(self, delay):
        self.c.after(delay)
        self.c.update()

    #######################################################################
    #  delete method                                                      #
    #                                                                     #
    #  Deletes the face from the canvas.  Note that the object still      #
    #  still exists after it is deleted; it is just not displayed.        #
    #######################################################################
    def delete(self, delay=5):
        self.c.after(delay)
        self.c.delete(self.tag)
        self.c.update()







