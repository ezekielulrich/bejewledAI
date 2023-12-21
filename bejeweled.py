from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get('https://www.bubbleshooter.net/game/bejeweled/')

playButton = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div[2]/a/div")
playButton.click()

# driver.quit()