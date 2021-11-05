import unittest
from time import sleep
from pyunitreport import HTMLTestRunner

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from faker import Faker


fake = Faker('en_US')

class UsingUnnittest(unittest.TestCase):

    def setUp(self):
        s = Service('./chromedriver')
        self.driver = webdriver.Chrome(service = s)
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com')

    def test_new_user(self):
        driver = self.driver
        account_link = driver.find_element(By.LINK_TEXT, 'ACCOUNT')
        account_link.click()
        login_link = driver.find_element(By.LINK_TEXT, 'Log In')
        login_link.click()
        create_account_button = driver.find_element(By.LINK_TEXT, 'CREATE AN ACCOUNT')
        create_account_button.click()
        import ipdb; ipdb.set_trace()
        first_name = driver.find_element(By.ID, 'firstname')
        first_name.send_keys(fake.first_name_female())
        middle_name = driver.find_element(By.ID, 'middlename')
        middle_name.send_keys(fake.first_name_female())
        last_name = driver.find_element(By.ID, 'lastname')
        last_name.send_keys(fake.last_name_female())
        email_address = driver.find_element(By.ID, 'email_address')
        email_address.send_keys(fake.ascii_safe_email())
        password = driver.find_element(By.ID, 'password')
        password.send_keys('password')
        confirm_password = driver.find_element(By.ID, 'confirmation')
        confirm_password.send_keys('password')
        newsletter = driver.find_element(By.ID, 'is_subscribed')
        newsletter.click()
        submit_button = driver.find_element(By.XPATH, '//*[@id="form-validate"]/div[2]/button')
        submit_button.click()


    def tearDown(self):
        print('Browser is about to close...')
        sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity = 2)
