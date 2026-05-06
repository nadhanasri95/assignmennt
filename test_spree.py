import pytest
from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.common.keys import Keys
import time

class TestSpreeProducts:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demo.spreecommerce.org/us/en/products")
        time.sleep(3)
        yield
        self.driver.quit()
    def test_product_name_and_price(self):
        products = self.driver.find_elements(By.CLASS_NAME, "group")
        assert len(products) > 0
        expected_products =[
            "Automated Expresso Machine",
            "semi-automated expresso machine",
            "drip coffee maker 1.5L"
        ]

        for product in products:
            name = product.find_element(By.TAG_NAME,"h3").text
            price = product.find_element(By.TAG_NAME, "span").text

            print(name,price)
            assert name != ""
            assert "$" in price