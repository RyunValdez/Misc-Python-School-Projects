from tkinter import *
c = Canvas(width=500, height=500, bg='white')
c.pack(expand=YES, fill=BOTH)

# attributes directly from parameters
left = 0
top = 0
width = 500
height = 500



# create X-coordinate guide list
xspaces = 40  # number of guides in the guide list
xgridwidth = 1.0 * width / xspaces
x = []
for i in range(xspaces+1):
    x.append(left + i*xgridwidth)

# create Y-coordinate guide list
yspaces = 40  # number of guides in the guide list
ygridwidth = 1.0 * height / yspaces
y = []
for i in range(yspaces+1):
    y.append(top + i*ygridwidth)


head =  ( ( x[10],y[12]) , ( x[12],y[6]) , (x[20], y[2]) , (x[28], y[6]) , (x[30], y[12]),
          (x[30], y[16]) , (x[28], y[28]) , (x[22], y[34]) , (x[18], y[34]),
          (x[12], y[28]) , (x[10], y[16]) , (x[10], y[12]))
hair = ( ( x[10],y[14]) , ( x[12],y[10]) , (x[15], y[7]) , (x[20], y[8]) , (x[25], y[7]),
          (x[28], y[10]) , (x[30], y[14]) )
lefteyebrow = ( ( x[12],y[13]) , ( x[14],y[12]) , (x[18], y[13]))
righteyebrow = ( ( x[28],y[13]) , ( x[26],y[12]) , (x[22], y[13]))
lefteye = ( ( x[12],y[16]) , ( x[15],y[15]) , (x[18], y[16]),( x[15],y[17]))
righteye = ( ( x[28],y[16]) , ( x[25],y[15]) , (x[22], y[16]),( x[25],y[17]))


# draw body
HeadID = c.create_polygon(head, fill="white", outline = "blue", smooth=1, width=3)
HairID = c.create_line(hair, fill="blue")
LeftEyebrowID = c.create_line(lefteyebrow, fill="blue", smooth = 1)
RightEyebrowID = c.create_line(righteyebrow, fill="blue", smooth = 1)
LeftEyeID = c.create_polygon(lefteye, fill="white", outline = "blue", smooth=1)
RightEyeID = c.create_polygon(righteye, fill="white", outline = "blue", smooth=1)



