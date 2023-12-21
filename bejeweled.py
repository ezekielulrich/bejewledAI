from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options

# Variables
url = 'https://www.bubbleshooter.net/game/bejeweled/'

# Create the mute driver to interact with the web version of Bejeweled
options = Options()
options.set_preference("media.volume_scale", "0.0")
driver = webdriver.Firefox(options=options)

# Open specified page
driver.get(url)

# Navigate to and click play button
playButton = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div[2]/a/div")
actions = ActionChains(driver)
actions.move_to_element(playButton).click().perform()

# Go fullscreen
fullscreen = driver.find_element(By.XPATH, '//*[@id="toggle_fullscreen"]')
actions.click(fullscreen).perform()

driver.quit()