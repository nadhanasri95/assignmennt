import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging

class TestProduct:

    @pytest.fixture
    def driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        yield self.driver
        logging.info("testing is completed")
        self.driver.quit()

    def test_open_site(self, driver):
        self.driver = driver
        driver.get("https://demo.spreecommerce.org/")
        time.sleep(3)
        assert "spreecommerce" in driver.current_url

    def test_purchase(self, driver):
        self.driver = driver

        self.driver.get("https://demo.spreecommerce.org/")
        time.sleep(3)


        driver.find_element(By.PARTIAL_LINK_TEXT, "Espresso").click()
        time.sleep(3)


        driver.find_element(By.XPATH, "//bu[contains(text(),'Add to Cart')]").click()



        cart = driver.find_element(By.XPATH, "//a[contains(@href,'/cart')]")
        driver.execute_script("arguments[0].click();", cart)

        time.sleep(5)


        assert "cart" in driver.current_url