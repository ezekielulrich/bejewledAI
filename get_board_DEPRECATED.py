from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.get('https://en.gameslol.net/data//bejeweled-hd//index.html')
time.sleep(15)
canvas = driver.find_element(By.XPATH, '//*[@id="GameCanvas"]')
click_to_start = ActionChains(driver)
click_to_start.move_to_element_with_offset(canvas, xoffset= -175, yoffset= 80).click().perform()
time.sleep(5)
click_to_start.move_to_element_with_offset(canvas, xoffset= 60, yoffset= -105).click().perform()
time.sleep(2)
click_to_start.move_to_element_with_offset(canvas, xoffset= 60, yoffset= -70).click().perform()


cell_size = 32*2
time.sleep(1)
click_to_start.move_to_element_with_offset(canvas, xoffset= 100 + cell_size/2, yoffset= -10 + cell_size/2).context_click().perform() #takes to center of board

