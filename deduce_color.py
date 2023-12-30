from PIL import Image
import numpy as np

path = r'C:\GIT_pulls\Bejeweled_ai\bejewledAI\images\gem_types\g.png'
image = Image.open(path)
width,height = image.size
#print(width, height)
nparray = np.array(image)
nparray = nparray.reshape((15625,4))
nparray = nparray[:,:3]
print(nparray.mean(axis=0))
keep = (nparray.max(axis=1)) > 100
nparray=nparray[keep]
nparray=nparray.mean(axis=0)
print(nparray)


"""
Colors resulting from this operation and to be used as bases:


.purple {
    background-color: rgb(201.56595745  26.76499033 201.59168279);
}
.green {
    background-color: rgb(30.55330213 205.4474779   60.81344254);
}
.yellow {
    background-color: rgb(228.03564284 197.75595563  28.08346972);
}
.orange {
    background-color: rgb(228.07877791 122.34991095  40.42224962);
}
.white {
    background-color: rgb(203.38956224 203.3921289  203.39997148);
}
.red {
    background-color: rgb(215.25508142  17.72851539  40.03185546);
}

"""


#a=0
#for i in nparray[0]:
#    b=(max(i[0],i[1],i[2]))-(min(i[0],i[1],i[2]))
#    if b>a:
#        a=b   USED TO DEDUCE GRAY AREA PARAMETERS

#print(a)
    
    
