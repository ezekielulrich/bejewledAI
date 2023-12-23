from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import time

def get_board(path):
    im=Image.open(path)
    im = im.crop((500,80,1500,1080)).save("board_test.png")


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
path = r'C:\GIT_pulls\Bejeweled_ai\bejewledAI\screenshot3.png'
time.sleep(3)
image = canvas.screenshot(path)
get_board(path)



