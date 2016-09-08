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
        
        # attributes directly from parameters
        self.c = canvas
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.faceColor = faceColor
        self.eyeColor = eyeColor
        self.pupilColor = pupilColor
        self.pose = pose
        self.name = name
        self.displayName = displayName

        # calculated attributes
        self.tag = Face.objectName + str(Face.objectNum)
        Face.objectNum += 1
        self.right = self.left + self.width
        self.bottom = self.top + self.height
        self.center = (self.left + self.right) / 2.0
        self.middle = (self.top + self.bottom) / 2.0

    #######################################################################
    #  draw method                                                        #
    #                                                                     #
    #  Draws the face according to the attributes, including size,        #
    #  position, colors, and pose portrayed.                              #
    #                                                                     #
    #  Common coordinates:                                                #
    #      face                                                           #
    #      eye1, eye2                                                     #
    #      pupil1, pupil2  (default position defined)                     #
    #                                                                     #
    #  Variable coordinates:                                              #
    #      smile                                                          #
    #      brow1, brow2                                                   #
    #      pupil1, pupil2  (overwritten by five emotions)                 #
    #                                                                     #
    #  Drawing:                                                           #
    #      Draw all shapes in their assigned coordinates.  The smile is   #
    #      a line for all faces except ECSTATIC, for which it is a        #
    #      smoothed polygon.                                              #
    #######################################################################
    def draw(self):

        # create X-coordinate guide list
        xspaces = 20  # number of guides in the guide list
        xgridwidth = 1.0 * self.width / xspaces
        x = []
        for i in range(xspaces+1):
            x.append(self.left + i*xgridwidth)

        # create Y-coordinate guide list
        yspaces = 20  # number of guides in the guide list
        ygridwidth = 1.0 * self.height / yspaces
        y = []
        for i in range(yspaces+1):
            y.append(self.top + i*ygridwidth)

        ###################################################################
        #                   Common Coordinates                            #
        ###################################################################
        
        # face guides (two points)
        face  = (   (x[1],y[0]) , (x[19],y[20])  )

        # eye guides (two points each)
        eye1  = (  ( x[5],y[5]) , ( x[9],y[9])  )
        eye2  = (  (x[11],y[5]) , (x[15],y[9])  )

        # pupil guides (two points each, will be changed by some poses)
        pupil1 = ( ( x[6],y[6]) ,  (x[8],y[8]) )
        pupil2 = ( (x[12],y[6]) , (x[14],y[8]) )

        ###################################################################
        #                 Variable Coordinates                            #
        ###################################################################
        
        # smile, eyebrow, and pupil guides
        if self.pose == Pose.HAPPY:
            # smiling mouth, raised and arched eyebrows
            smile =  ( ( x[4],y[12]) , ( x[6],y[16]) , (x[14],y[16]) , (x[16],y[12]) )
            brow1 =  ( ( x[5], y[4]) , ( x[6], y[2]) , ( x[8], y[2]) , ( x[9], y[4]) )
            brow2 =  ( (x[11] ,y[4]) , (x[12] ,y[2]) , (x[14], y[2]) , (x[15], y[4]) )
        elif self.pose == Pose.GLAD:
            # mildly smiling mouth, raised eyebrows
            smile =  ( ( x[4],y[14]) , ( x[6],y[16]) , (x[14],y[16]) , (x[16],y[14]) )
            brow1 =  ( ( x[5], y[4]) ,  (x[6], y[3]) , ( x[8], y[3]) , ( x[9], y[4]) )
            brow2 =  ( (x[11] ,y[4]) , (x[12] ,y[3]) , (x[14], y[3]) , (x[15], y[4]) )
        elif self.pose == Pose.NEUTRAL:
            # straight mouth, straight eyebrows
            smile =  ( ( x[4],y[14]) , ( x[6],y[14]) , (x[14],y[14]) , (x[16],y[14]) )
            brow1 =  ( ( x[5], y[4]) ,  (x[6], y[4]) , ( x[8], y[4]) , ( x[9], y[4]) )
            brow2 =  ( (x[11] ,y[4]) , (x[12] ,y[4]) , (x[14], y[4]) , (x[15], y[4]) )
        elif self.pose == Pose.ANGRY:
            # mild frowning mouth, eyebrows angled in, pupils crossed
            smile =  ( ( x[4],y[15]) , ( x[6],y[13]) , (x[14],y[13]) , (x[16],y[15]) )
            brow1 =  ( ( x[5], y[4]) , ( x[6], y[3]) , ( x[8], y[3]) , ( x[9], y[5]) )
            brow2 =  ( (x[11], y[5]) , (x[12], y[3]) , (x[14], y[3]) , (x[15], y[4]) )
            pupil1 = ( ( x[7], y[6]) , ( x[9], y[8]) )
            pupil2 = ( (x[11], y[6]) , (x[13], y[8]) )
        elif self.pose == Pose.SAD:
            # frowning mouth, eyebrows angled out, pupils down
            smile =  ( ( x[4],y[16]) , ( x[6],y[12]) , (x[14],y[12]) , (x[16],y[16]) )
            brow1 =  ( ( x[5], y[5]) , ( x[6], y[3]) , ( x[8], y[3]) , ( x[9], y[4]) )
            brow2 =  ( (x[11], y[4]) , (x[12], y[3]) , (x[14], y[3]) , (x[15], y[5]) )
            pupil1 = ( ( x[6], y[7]) , ( x[8], y[9]) )
            pupil2 = ( (x[12], y[7]) , (x[14], y[9]) )
        elif self.pose == Pose.SMIRK:
            # asymetrically curved mouth and eyebrows, one pupil looking up
            smile =  ( ( x[4],y[14]) , ( x[6],y[12]) , (x[14],y[16]) , (x[16],y[14]) )
            brow1 =  ( ( x[5], y[4]) , ( x[6], y[3]) , ( x[8], y[3]) , ( x[9], y[2]) )
            brow2 =  ( (x[11], y[3]) , (x[12], y[2]) , (x[14], y[3]) , (x[15], y[4]) )
            pupil1 = ( ( x[6], y[6]) , ( x[8], y[8]) )
            pupil2 = ( (x[12], y[5]) , (x[14], y[7]) )
        elif self.pose == Pose.ECSTATIC:
            # open mouth, eyebrows arched high, pupils looking up
            smile =  ( ( x[4],y[13]) , ( x[6],y[16]) , (x[14],y[16]) ,
                       (x[16],y[13]) , ( x[4],y[13]) )
            brow1 =  ( ( x[5], y[4]) , ( x[6], y[2]) , ( x[8], y[2]) , ( x[9], y[4]) )
            brow2 =  ( (x[11], y[4]) , (x[12], y[2]) , (x[14], y[2]) , (x[15], y[4]) )
            pupil1 = ( ( x[6], y[6]) , ( x[8], y[8]) )
            pupil2 = ( (x[12], y[6]) , (x[14], y[8]) )
        elif self.pose == Pose.DRUNK:
            # curvy smile, eyebrows angled, one pupil looking down, one pupil looking in
            smile =  ( ( x[4],y[13]) , ( x[6],y[15]) , (x[10],y[13]) ,
                       (x[14],y[15]) , (x[16],y[13]) )
            brow1 =  ( ( x[5], y[5]) , ( x[6], y[4]) , ( x[8], y[4]) , ( x[9], y[3]) )
            brow2 =  ( (x[11], y[3]) , (x[12], y[4]) , (x[14], y[4]) , (x[15], y[5]) )
            pupil1 = ( ( x[6], y[7]) , ( x[8], y[9]) )
            pupil2 = ( (x[11], y[6]) , (x[13], y[8]) )
        elif self.pose == Pose.ANXIOUS:
            # curvy frown, eyebrows angled slightly
            smile =  ( ( x[4],y[15]) , ( x[6],y[13]) , (x[10],y[15]) ,
                       (x[14],y[13]) , (x[16],y[15])  )
            brow1 =  ( ( x[5], y[4]) , ( x[6] ,y[4]) , ( x[8], y[4]) , ( x[9], y[5]) )
            brow2 =  ( (x[11], y[5]) , (x[12], y[4]) , (x[14], y[4]) , (x[15], y[4]) )
        else:  # print warning message, unimplemented emotion
            print ("Error -- unimplemented pose")

        ###################################################################
        #                   Drawing                                       #
        ###################################################################
        
        # draw face
        self.faceID = self.c.create_oval(face, fill=self.faceColor, tag=self.tag)

        # draw eyes
        self.leftEyeID = self.c.create_oval(eye1, fill=self.eyeColor, tag=self.tag)
        self.rightEyeID = self.c.create_oval(eye2, fill=self.eyeColor, tag=self.tag)

        # draw pupils
        self.leftPupilID = self.c.create_oval(pupil1, fill=self.pupilColor, tag=self.tag)
        self.rightPupilID = self.c.create_oval(pupil2, fill=self.pupilColor, tag=self.tag)

        # draw smile (Variable Shape)
        if self.pose == Pose.ECSTATIC:  # Ecstatic has closed polygon for mouth)
            self.c.create_polygon(smile, width=2, fill="black", smooth=1, tag=self.tag)
        else:  # all other faces have open lines for mouth
            self.c.create_line(smile, width=2, fill="black", smooth=1, tag=self.tag)

        # draw brows 
        self.c.create_line(brow1, width=2, fill="black", smooth=1, tag=self.tag)
        self.c.create_line(brow2, width=2, fill="black", smooth=1, tag=self.tag)

        # draw name
        if self.displayName:  # only display if displayName flag is set
            self.c.create_text(self.center, self.bottom, anchor=N,
                               text=self.name, tag=self.tag)

        self.c.update()
        
    #######################################################################
    #  move method                                                        #
    #                                                                     #
    #  Moves the face on the canvas, relative to its current position,    #
    #  after the specified delay.  Attributes are adjusted accordingly.   #
    #######################################################################
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

    #######################################################################
    #  setProperties method                                               #
    #                                                                     #
    #  Changes the colors of the face, eyes, and pupils.  If a color is   #
    #  not specified, then it remains unchanged.                          #
    #######################################################################
    def setProperties (self, faceColor="default", eyeColor="default",
                       pupilColor="default"):
        if faceColor != "default":
            self.faceColor=faceColor
            self.c.itemconfig(self.faceID, fill=self.faceColor)
            self.c.update()
        if eyeColor != "default":
            self.eyeColor=eyeColor
            self.c.itemconfig(self.leftEyeID, fill=self.eyeColor)
            self.c.itemconfig(self.rightEyeID, fill=self.eyeColor)
            self.c.update()
        if pupilColor != "default":
            self.pupilColor=pupilColor
            self.c.itemconfig(self.leftPupilID, fill=self.pupilColor)
            self.c.itemconfig(self.rightPupilID, fill=self.pupilColor)
            self.c.update()

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







