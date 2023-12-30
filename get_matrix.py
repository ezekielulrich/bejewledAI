import numpy as np
from numpy.linalg import norm
from PIL import Image
import os

names = ["g", "o", "p", "r", "y", "w"]
colors=np.array([[30.55330213, 205.4474779 ,  60.81344254],
                 [228.07877791, 122.34991095 , 40.42224962],
                 [201.56595745 , 26.76499033, 201.59168279],
                 [215.25508142 , 17.72851539 , 40.03185546],
                 [228.03564284 ,197.75595563,  28.08346972],
                 [203.38956224 ,203.3921289 , 203.39997148]])

array = []
path=r'C:\GIT_pulls\Bejeweled_ai\bejewledAI\images\boards\board_test2.png'


def deduce_color(image):
    #image = Image.open(path)
    nparray = np.array(image)
    nparray = nparray.reshape((15625,4))
    nparray = nparray[:,:3]
    keep = (nparray.max(axis=1)) > 100
    nparray=nparray[keep]
    nparray=nparray.mean(axis=0)
    return(nparray)



im=Image.open(path)
width,height=im.size

width/=8
height/=8

for y in range(8):
    for x in range(8):
        final_mean = float('inf')
        final_color = "NONE"
        left=x*width
        top=y*height
        right=left+width
        bottom=top+height
        im1=np.array(im.crop((left,top,right,bottom)))
        cell_color = deduce_color(im1)
        for i in range(len(colors)):
            mean_dif = np.absolute(cell_color-colors[i])
            #print(names[i], mean_dif, end=' ')
            mean_dif = (mean_dif[0]+mean_dif[1]+mean_dif[2])/3
            #print(mean_dif)
            if mean_dif < final_mean:
                final_mean = mean_dif
                final_color = names[i]
        array.append(final_color)

for i in range(64):
    print(array[i], end=" ")
    if (i+1)%8==0:
        print()