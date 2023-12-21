from selenium import webdriver
from selenium.webdriver.common.by import By

# Variables
url = 'https://www.bubbleshooter.net/game/bejeweled/'

# Create the driver to interact with the web version of Bejeweled
driver = webdriver.Firefox()

# Open specified page
driver.get(url)

# Navigate to and click play button
playButton = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div[2]/a/div")
playButton.click()

# Use computer vision to interact from here on

driver.quit()