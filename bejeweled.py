from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Variables
url = 'https://www.bubbleshooter.net/game/bejeweled/'

# Functions

# Create the driver to interact with the web version of Bejeweled
driver = webdriver.Firefox()

# Open specified page
driver.get(url)

# Navigate to and click play button
playButton = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div[2]/a/div")
actions = ActionChains(driver)
actions.move_to_element(playButton).click()

# Allow time for game to load
actions.pause(5)


driver.quit()