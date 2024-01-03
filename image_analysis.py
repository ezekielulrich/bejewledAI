import opencv as cv2
import numpy as np
import selenium

def getPlayingFieldInfo(self): 
    # Responsible for getting the information 
    img = self.getWindowShot() 
    (x, y, w, h) = self._getPlayingFieldCoord(img) 
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
    # The ordering for the limits follows: 
    # 1) Red 
    # 2) White 
    # 3) Yellow 
    # 4) Blue 
    # 5) Purple 
    # 6) Orange 
    # 7) Green 
    croppedImage = img[y:y+h, x:x+w] 
    colors = [ "R", "W", "Y", "B", "P", "O", "G" ] 
    lowerLimits = [ 
        np.array([0, 0, 128]), 
        np.array([200, 200, 200]), 
        np.array([0, 128, 128]), 
        np.array([128, 128, 0]), 
        np.array([128, 0, 128]), 
        np.array([0, 64, 170]), 
        np.array([32, 150, 32]) 
    ] 
    higherLimits = [ 
        np.array([0, 0, 255]), 
        np.array([255, 255, 255]), 
        np.array([0, 255, 255]), 
        np.array([255, 255, 0]), 
        np.array([255, 0, 255]), 
        np.array([0, 128, 255]), 
        np.array([150, 255, 150]) 
    ] 
    matrix = [ 
        [0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0] 
    ] 
    for multipleY in range(1,9): 
        for multipleX in range(1,9): 
            imgSeg = croppedImage[12 + (52*(multipleY-1)):12 + (52*multipleY), 12 + (52*(multipleX-1)):12 + (52*(multipleX))] 
            highestCount = 0 
            theColor = "N/A" 
            for (lower, higher, color) in zip(lowerLimits, higherLimits, colors): 
                filteredImg = cv2.inRange(imgSeg, lower, higher)
                uniques, counts = np.unique(filteredImg, return_counts=True) 
                counts = dict(zip(uniques, counts)) 
                if 255 in counts and counts[255] > highestCount: 
                    highestCount = counts[255] 
                    theColor = color 
            matrix[multipleY-1][multipleX-1] = theColor 
    return matrix

def _getPlayingFieldCoord(self, img): 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    gray = cv2.GaussianBlur(gray, (3, 3), 3) 
    canny = cv2.Canny(gray, 50, 100) 
    _, cnts, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
    contour = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
    return cv2.boundingRect(contour)



def getWindowShot(self): 
    region = self.getWindowDimensions() 
    img = pyautogui.screenshot(region=region) 
    return np.array(img)

_getPlayingFieldCoord(self, "screenshot.png")