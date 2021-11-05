import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class UsingUnnittest(unittest.TestCase):

    def setUp(self):
        s = Service('./chromedriver')
        self.driver = webdriver.Chrome(service = s)
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com')

    def test_select_language(self):
        driver = self.driver
        language_selector = Select(driver.find_element(By.ID, 'select-language'))
        language_selector.select_by_visible_text('German')
        sleep(1)
        language_selector = Select(driver.find_element(By.ID, 'select-language'))
        language_selector.select_by_index(1)
        sleep(1)

    def tearDown(self):
        print('Browser is about to close...')
        sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity = 2)
