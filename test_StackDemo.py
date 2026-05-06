import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import time


class TestBrowserStackDemo:

    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        time.sleep(3)
        logging.info("testing is completed")
        driver.quit()

    def test_open_website(self, driver):
        driver.get("https://bstackdemo.com/")
        assert "StackDemo" in driver.title

    def test_add_product_to_cart(self, driver):
        driver.get("https://bstackdemo.com/")
        time.sleep(3)


        add_to_cart = driver.find_element(By.XPATH, "(//div[text()='Add to cart'])[1]")
        add_to_cart.click()
        time.sleep(3)


        cart_header = driver.find_element(By.CLASS_NAME, "float-cart__headerr")
        assert cart_header.is_displayed()

        print("Product added and cart opened successfully")