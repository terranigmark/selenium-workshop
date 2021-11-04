import unittest
from time import sleep
from pyunitreport import HTMLTestRunner

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class UsingUnnittest(unittest.TestCase):

    def setUp(self):
        s = Service('./chromedriver')
        self.driver = webdriver.Chrome(service = s)

    def test_get_ptyhon_website(self):
        driver = self.driver
        driver.get('https://www.python.org')
        driver.find_element(By.CLASS_NAME, 'tier-1')
        driver.find_element(By.CSS_SELECTOR, '#community')
        driver.find_element(By.ID, 'downloads')
        driver.find_element(By.LINK_TEXT, 'About')
        driver.find_element(By.NAME, 'q')
        driver.find_element(By.TAG_NAME, 'h1')
        driver.find_element(By.XPATH, '//*[@id="touchnav-wrapper"]/header/div/div[1]/a')

    def tearDown(self):
        print('Browser is about to close...')
        sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(
        verbosity = 2,
        testRunner = HTMLTestRunner(
            output = 'report',
            report_name = 'python_org_report',
            failfast = True))
