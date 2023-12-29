import numpy as np
from numpy.linalg import norm
from PIL import Image
import os

names = ["g", "o", "p", "r", "y", "w"]

array = []
path=r'C:\GIT_pulls\Bejeweled_ai\bejewledAI\images\boards\board_test2.png'

im=Image.open(path)
width,height=im.size

width/=8
height/=8

for x in range(8):
    for y in range(8):
        final_difference = float('inf')
        final_color = "NONE"
        left=x*width
        top=y*height
        right=left+width
        bottom=top+height
        im1=np.array(im.crop((left,top,right,bottom)))
        for color in range(len(names)):
            imagename = names[color]+".png"
            path = os.path.join(r'C:\GIT_pulls\Bejeweled_ai\bejewledAI\images\gem_types', imagename)
            im2 = np.array(Image.open(path))
            difference = norm(im2 - im1)
            if difference < final_difference:
                final_difference = difference
                final_color = names[color]
        array.append(final_color)

for i in range(64):
    print(array[i], end=" ")
    if (i+1)%8==0:
        print()