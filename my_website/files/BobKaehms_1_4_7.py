'''
BobKaehms_1_4_7: Change pixels in an image.
This example first changes the background,
then mirrors in the X-axis, then the Y-axis

This example uses matplotlib to manipulate the image at the pixel level.  
The next iteration will use the PIL Image library

'''
from PIL import Image
import matplotlib.pyplot as plt
import os.path
import numpy as np  # "as" lets us use standard abbreviations
   
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
#filename = os.path.join(directory, 'chrysler-top-bw1.jpg')
#filename = os.path.join(directory, 'chrysler-top-rgb-sm.jpg')
filename = os.path.join(directory, 'grads.jpg')
# Read the image data into an array
img = plt.imread(filename)
imgdest = plt.imread(filename)

fig, ax = plt.subplots(1, 1)



height = len(img)
width = len(img[0])
print ('width= ',width)
print ('height= ',height)


def changeBG(im,r,g,b,tol): 
    ''' flip all the bits that are greater than a certain combined (rgb) value), usually background'''       
    for row in range(height):
        for col in range(width):
            if sum(im[row][col])>tol:
                im[row][col] = [r,b,g]  
                
def mirrorImgX(im):
    ''' mirror the image across the x-axis '''
    for row in range(height):
        for col in range(width/2):
#            print (row,col,width-col,height-row)
            r=im[row][col][0]
            g=im[row][col][1]
            b=im[row][col][2]
            
            im[row][width-col-1][0]=r
            im[row][width-col-1][1]=g 
            im[row][width-col-1][2]=b  
                    
def mirrorImgY(im):
    ''' mirror the image across the y-axis '''
    for row in range(height/2):
        for col in range(width):
#            print (row,col,width-col,height-row)
            r=im[row][col][0]
            g=im[row][col][1]
            b=im[row][col][2]
            
            im[height - row-1][col][0]=r
            im[height - row-1][col][1]=g 
            im[height - row-1][col][2]=b 
             
def pixelateG(im,xr,yr): 
    ''' sample the image at center of an x,y bounding rectangle, then fill all bits in that rectangle with the sampled rgb value'''       
    xstep=xr/2
    xrange=width/xr
    ystep=yr/2  
    yrange=height/yr
    
    for nextX in range(xrange):
        for nextY in range(yrange):
            nextXc=(nextX-1) * xr + xstep
            nextYc=(nextY-1) * yr + ystep
             
            r=im[nextYc][nextXc][0]
            g=im[nextYc][nextXc][1]
            b=im[nextYc][nextXc][2]
            
            for xfill in range(nextXc-xstep,nextXc+xstep):
                for yfill in range(nextYc-ystep,nextYc+ystep):
                    im[xfill,yfill]=[r,g,b]
            
            
             
                
                
#changeBG(img,100,100,255,500)
changeBG(img,56,148,67,500)
#pixelateG(img,50,50)
mirrorImgY(img)
mirrorImgX(img)        

                    
# Show the image data in a subplot
ax.imshow(img, interpolation='none')


        
# Show the figure on the screen
#print(type(img))

fig.show()