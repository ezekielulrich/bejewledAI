from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options

from PIL import Image

import numpy as np

# Variables
# Using this random bootleg online version of Bejewled
url = 'https://en.gameslol.net/data//bejeweled-hd//index.html'

# Accepts a pillow image and converts to a numpy matrix
def convert(image: Image) -> np.ndarray:
    # Get the image dimensions
    width, height = image.size

    # Convert the image to RGB
    image = image.convert('RGB')

    # Convert the image data to a numpy array
    data = np.array(image)

    # Define a mapping from color values to gem characters
    # TODO: Check within a range to make more robust
    color_to_gem = {
        (251, 25, 55): 'R',  # Red gem
        (5, 153, 30): 'G',  # Green gem
        (255, 246, 34): 'Y',  # Yellow gem
        (215, 113, 29): 'O',  # Orange gem
        (241, 15, 244): 'P',  # Pink gem
        (250, 250, 250): 'W',  # White gem
    }

    # Create an empty matrix to hold the gem characters
    gem_matrix = np.empty((8,8), dtype='object')

    # Iterate over each cell
    for i in range(8):
        for j in range(8):

            # Define the region to sample
            region = image.crop(((j + 0.375) * width / 8, (i + 0.375) * height / 8, (j + 0.625) * width / 8, (i + 0.625) * height / 8))

            # Calculate the average color of the region
            color = np.mean(np.array(region), axis=(0, 1))

            # Calculate the Euclidean distance to each color in the mapping
            distances = {gem: np.linalg.norm(np.array(color) - np.array(gem_color)) for gem_color, gem in color_to_gem.items()}

            # Get the color with the smallest distance
            nearest_color = min(distances, key=distances.get)

            gem_matrix[i, j] = nearest_color
    
    return gem_matrix

def load(url: str):

    # Create the mute driver to interact with the web version of Bejeweled
    options = Options()
    options.set_preference("media.volume_scale", "0.0")
    driver = webdriver.Firefox(options=options)

    # Open specified page
    driver.get(url)

    actions = ActionChains(driver)

    # Click classsic mode
    '''
    driver.implicitly_wait(20)
    canvas = driver.find_element(By.XPATH, '//*[@id="GameCanvas"]')
    print("Found element")

    actions.pause(10)
    actions.move_to_element_with_offset(canvas, -112, -84).perform()
    actions.pause(10)
    actions.click().perform()
    actions.pause(10)
    '''

    #return driver
    driver.quit()

print(convert(Image.open(r"images\board.png")))
# making a matrix

# machine learning

# making a move