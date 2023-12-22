from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import cv2
from PIL import Image
import time


driver = webdriver.Firefox()

driver.get('https://en.gameslol.net/data//bejeweled-hd//index.html')
time.sleep(15)
canvas = driver.find_element(By.XPATH, '//*[@id="GameCanvas"]')
click_to_start = ActionChains(driver)
click_to_start.move_to_element_with_offset(canvas, xoffset= -175, yoffset= 80).click().perform()
time.sleep(5)
click_to_start.move_to_element_with_offset(canvas, xoffset= -175, yoffset= 80).context_click().perform()


"""time.sleep(5)
path = r'C:\GIT_pulls\Bejeweled_ai\bejewledAI\screenshot3.png'

image = canvas.screenshot(path)
im=Image.open(path)
im = im.crop((555,80,1705,1240)).save("board_test.png")"""

