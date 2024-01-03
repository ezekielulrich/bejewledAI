from PIL import Image

path=r'C:\GIT_pulls\Bejeweled_ai\bejewledAI\images\boards\board_test2.png'

im=Image.open(path)
width,height=im.size

width/=8
height/=8

left=3*width
top=3*height
right=left+width
bottom=top+height

path = r'C:\GIT_pulls\Bejeweled_ai\bejewledAI\images\gem_types\w.png'

im1=im.crop((left,top,right,bottom)).save(path)
#im1.show()
