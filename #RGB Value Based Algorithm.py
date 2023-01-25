#RGB Value Based Algorithm
#Created by Brandon Robinson
from PIL import Image
import os
from settings import *
import random
#Method Of choice??
if meth1==False and meth2==False and meth3==False:
    print("Error: Please select a method!")
    os._exit(1)
try:
    os.chdir('Desktop')
except:
    pass
#Value Section
ValueAlt=26
horizontal=0 #Incoming image resolution
horizontal_CURRENT_WRITE=0 #Memory for next drawable pixel on horizontal scale after calculations +1
horizontal_CURRENT_READ=0 #Memory for next readable pixel on horizontal scale after calculations +1
vertical=0 #Incoming image resolution
vertical_CURRENT_WRITE=0 #Memory for net down section +1
vertical_CURRENT_READ=0 #Memory for next down section +1
#image = Image.new('RGB', horizontal, vertical)

#Get dimensions of incoming file:
im = Image.open('test.jpg') # Can be many different formats.
pix = im.load()
horizontal, vertical = im.size  # Get the width and hight of the image for iterating over
#Create dimensions for outgoing file:
output=Image.new('RGB', (horizontal, vertical))

def main():
    global horizontal, vertical, meth1, meth2, meth3
    for i in range(horizontal*vertical):
        try:
            r, g, b = readPixel()
            if meth1==True:
                r, g, b = AlterRGBMethod1(r, g, b)
            if meth2==True:
                r, g, b = AlterRGBMethod2(r, g, b)
            if meth3==True:
                r, g, b = AlterRGBMethod3(r, g, b)
            placePixel(r, g, b)
        except TypeError:
            print(i)
            break\

def AlterRGBMethod1(r, g, b):
    return r, g, b

def AlterRGBMethod2(r, g, b):
    return r, g, b

def AlterRGBMethod3(r, g, b):
    r+=random.randint(1,5)
    g+=random.randint(1,5)
    b+=random.randint(1,5)
    return r, g, b

def readPixel(var=None):
    '''Return RGB Values from automated cords. Values retrieved from input image.\n RGB are returned as 3 seperate vars.'''
    global im, horizontal_CURRENT_READ, vertical_CURRENT_READ, horizontal, vertical, debug
    ignoreNextAdd=False
    if horizontal_CURRENT_READ == horizontal-1: #Checks
        horizontal_CURRENT_READ=0 #Set to 0
        vertical_CURRENT_READ+=1 #Adds 1, does not overwrite.
        ignoreNextAdd=True
    try:
        r, g, b = pix[horizontal_CURRENT_READ, vertical_CURRENT_READ]
    except IndexError:
        print('IndexError: ',horizontal_CURRENT_READ, vertical_CURRENT_WRITE)
        exit
    if ignoreNextAdd==False:
        horizontal_CURRENT_READ+=1
    try:
        if debug == True:
            print('System Read:  Horizontal: '+str(horizontal_CURRENT_READ)+' Vertical: '+str(vertical_CURRENT_READ))
        return r, g, b
    except:
        pass 

def placePixel(r, g, b):
    '''Places a pixel going horizontally until it reaches the end, then moves down 1 vertically'''
    #image.putpixel((horizontal, vertical), (colorSet)) to draw pixel
    global horizontal_CURRENT_WRITE, vertical_CURRENT_WRITE, horizontal, vertical, debug, output
    list = ['r', 'g', 'b']
    passed=True
    for i in range(3):
        if locals()[list[i]] < 0:
            passed = False
        if locals()[list[i]] > 255:
            passed = False
    if passed == False:
        print("Error detected, problems may occur. Passed = False, placePixel()")
    if passed==True:
        ignoreNextAdd=False
        if horizontal_CURRENT_WRITE == horizontal-1: #Checks
            horizontal_CURRENT_WRITE=0 #Set to 0
            vertical_CURRENT_WRITE+=1 #Adds 1, does not overwrite.
            ignoreNextAdd=True
        output.putpixel((horizontal_CURRENT_WRITE, vertical_CURRENT_WRITE), (r, g, b))
        if ignoreNextAdd==False:
            horizontal_CURRENT_WRITE+=1
        if debug==True:
            print("System Write: Horizontal: "+str(horizontal_CURRENT_WRITE)+'  Vertical: '+str(vertical_CURRENT_WRITE))


'''from PIL import Image

im = Image.open('dead_parrot.jpg') # Can be many different formats.
pix = im.load()
print im.size  # Get the width and hight of the image for iterating over
print pix[x,y]  # Get the RGBA Value of the a pixel of an image
pix[x,y] = value  # Set the RGBA Value of the image (tuple)
im.save('alive_parrot.png')  # Save the modified pixels as .png

'''




main()
output.save('output.png')