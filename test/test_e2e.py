import pytest
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.NAME, "name").send_keys("Rahul")
        self.driver.find_element(By.NAME, "email").send_keys("rahulshetty@gmail.com")
        self.driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
        self.driver.find_element(By.CLASS_NAME, "form-check-label").click()
