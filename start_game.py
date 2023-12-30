from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import time

def get_board(path):
    im=Image.open(path)
    im = im.crop((500,80,1500,1080)).save(r"images\boards\board_test3.png")

def make_move(cell, direction):
    time.sleep(1)
    cell_size = 64
    x=(cell % 8) - 4
    y=int(cell / 8) - 4
    click_to_start.move_to_element_with_offset(canvas, xoffset= 100 + cell_size/2 + x*cell_size, yoffset= -10 + cell_size/2 + y*cell_size).click().perform()
    if direction == "u":
        y-=1
    elif direction == "r":
        x-=1
    elif direction == "d":
        y+=1
    elif direction=="l":
        x+=1
    time.sleep(0.2)
    click_to_start.move_to_element_with_offset(canvas, xoffset= 100 + cell_size/2 + x*cell_size, yoffset= -10 + cell_size/2 + y*cell_size).click().perform()



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


directions = ["u", "r", "d", "l"]
make_move(24,"u")
make_move(28,"d")
path = r'C:\GIT_pulls\Bejeweled_ai\bejewledAI\images\boards\screenshot4.png'
time.sleep(3)
image = canvas.screenshot(path)
get_board(path)



