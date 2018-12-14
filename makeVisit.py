#!/usr/bin/env python3
import sys
import os


from visit_utils import *
# import visit_utils, we will use it to help encode our movie
DeleteAllPlots()

# Step 1:Open the database 
# Step 2: Add plots
# Print available operators
print OperatorPlugins()

OpenDatabase('data.vts')
AddPlot("Pseudocolor", "phi")

OpenDatabase('mesh.vtk')
AddPlot("Mesh", "mesh")
iso_atts = IsosurfaceAttributes()
iso_atts.variable = "phi"
AddOperator("Isosurface")
DrawPlots()
for i in range(30):
    iso_atts.contourValue = (2 +0.1*i)
    SetOperatorOptions(iso_atts)
      

#Slice the volume to show only three
# external faces, and add an Isovolume operator
AddOperator("Isovolume")
AddOperator("ThreeSlice",1)
tatts = ThreeSliceAttributes()
tatts.x = 0
tatts.y = 0
tatts.z = 0
SetOperatorOptions(tatts)

# Step 3: Draw the plots
DrawPlots()
SaveWindow()

Query("Max")
val = GetQueryOutputValue()
print "Max value of 'phi' = ", val


# Set a blue/black, radial, gradient background.
a = AnnotationAttributes()
a.backgroundMode = a.Gradient
a.gradientBackgroundStyle = a.Radial
a.gradientColor1 = (0,0,255,255) # Blue
a.gradientColor2 = (0,0,0,255) # Black
SetAnnotationAttributes(a)
SaveWindow()


#AddOperator("Slice", 1) 
#a = SliceAttributes()
#a.originType=a.Point
#a.normal, a.upAxis = (0,0,1), (0,1,0)
# Only set the attributes for the selected plot.
#SetOperatorOptions(a)
#DrawPlots()


# Get an initialized 3D view object.
# Rotate the plots interactively.
ResetView()
v = GetView3D()

v.viewNormal = (-0.571619, 0.405393, 0.713378)
v.viewUp = (0.308049, 0.911853, -0.271346)

SetCenterOfRotation(-4.755280, 6.545080, 5.877850)
v.RotateAxis(0,-65)
v.RotateAxis(1,90)
SetView3D(v)



# Step 4: Animate through time and save images
#for states in range(TimeSliderGetNStates()):
#  SetTimeSliderState(states)


# get the number of timesteps
nts = TimeSliderGetNStates()
 
# set basic save options
swatts = SaveWindowAttributes()
#
# The 'family' option controls if visit automatically adds a frame number to 
# the rendered files. For this example we will explicitly manage the output name.
#
swatts.family = 0

# select PNG as the output file format

swatts.format = swatts.PNG 

# set the width of the output image

swatts.width = 1024 

# set the height of the output image

swatts.height = 1024
 
#the encoder expects file names with an integer sequence
# 0,1,2,3 .... N-1
 
file_idx = 0
 
for ts in range(0,nts,10): # look at every 10th frame
    # Change to the next timestep
    TimeSliderSetState(ts)
  #before we render the result, explicitly set the filename for this render
    swatts.fileName = "Data_Proj_%04d.png" % file_idx
    SetSaveWindowAttributes(swatts)
    # render the image to a PNG file
    SaveWindow()
    file_idx +=1
input_pattern = "Data_Proj_%04d.png"
output_movie = "Data_Proj.wmv"
encoding.encode(input_pattern,output_movie,fdup=4)






