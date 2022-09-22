from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

_Driver = webdriver.Edge("./msedgedriver.exe")

_Driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')

nObjects = 7

time.sleep(3)

actions = ActionChains(_Driver)

for i in range(1, nObjects + 1):
  card = _Driver.find_element(By.ID, f'box{i}')
  box = _Driver.find_element(By.ID, f'box10{i}')
  actions.drag_and_drop(card, box).perform()

time.sleep(2)

_Driver.quit()