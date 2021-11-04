import unittest
from time import sleep
from pyunitreport import HTMLTestRunner

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class UsingUnnittest(unittest.TestCase):

    def setUp(self):
        s = Service('./chromedriver')
        self.driver = webdriver.Chrome(service = s)

    def test_get_ptyhon_website(self):
        driver = self.driver
        driver.get('https://www.python.org')
        driver.find_element_by_link_text('About').click()

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
