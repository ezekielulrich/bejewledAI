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
    # Convert the image to RGB
    image = image.convert('RGB')

    # Convert the image data to a numpy array
    data = np.array(image)

    # Define a mapping from color values to gem characters
    color_to_gem = {
        (247, 25, 54): 'R',  # Red gem
        (0, 255, 0): 'G',  # Green gem
        (0, 0, 255): 'Y',  # Yellow gem
        (0, 0, 255): 'O',  # Orange gem

        # Add more colors as needed
    }

    # Create an empty matrix to hold the gem characters
    gem_matrix = np.empty(data.shape[:2], dtype='object')

    # Iterate over each pixel in the image
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            # Get the color of the pixel
            color = tuple(data[i, j])

            # Map the color to a gem character
            gem = color_to_gem.get(color, ' ')

            # Add the gem character to the matrix
            gem_matrix[i, j] = gem

    return gem_matrix

def load(url):

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

load(url)
# making a matrix

# machine learning

# making a move