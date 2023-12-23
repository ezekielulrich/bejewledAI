#import cv2
from PIL import Image


path = r'C:\GIT_pulls\Bejeweled_ai\bejewledAI\screenshot3.png'

im=Image.open(path)
im = im.crop((500,80,1500,1080)).save("board_test.png")
