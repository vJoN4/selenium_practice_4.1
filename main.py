from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import HtmlTestRunner
import unittest
import time

# ! NOTE: Unittest derives from PyUnit
class DragAndDrop(unittest.TestCase):

  def setUp(self):
    self.nObjects = 7
    self._Driver = webdriver.Edge("./msedgedriver.exe")
    self._Driver.maximize_window()
    self._Driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')

  def test_drag_and_drop(self):
    actions = ActionChains(self._Driver)

    for i in range(1, self.nObjects + 1):
      card = self._Driver.find_element(By.ID, f'box{i}')
      box = self._Driver.find_element(By.ID, f'box10{i}')
      actions.drag_and_drop(card, box).perform()

    time.sleep(2)

    self._Driver.quit()

if __name__ == '__main__':
  unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))