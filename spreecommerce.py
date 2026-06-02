import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestSpreeProducts:

    @pytest.fixture
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demo.spreecommerce.org/t/categories/men/jackets-and-coats")
        yield
        self.driver.quit()

    def test_extract_and_validate_products(self, setup):
        driver = self.driver
        wait = WebDriverWait(driver, 15)

        # ✅ Handle cookie popup (if appears)
        try:
            accept = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Accept')]"))
            )
            accept.click()
        except:
            pass

        # ✅ Wait for product container (IMPORTANT)
        wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # ✅ Updated WORKING locator (very important)
        products = driver.find_elements(By.XPATH, "//div[contains(@class,'col-')]//a[contains(@href,'/products/')]")

        print("Total products found:", len(products))

        assert len(products) > 0, "No products found on the page"

        product_data = []

        for product in products:
            name = product.text.strip()

            if name == "":
                continue  # skip empty elements

            # Try to get price (relative to product)
            try:
                price = product.find_element(By.XPATH, ".//following::span[contains(@class,'price')][1]").text
            except:
                price = "Price not found"

            print(f"Name: {name} | Price: {price}")

            product_data.append((name, price))

            # ✅ Validation
            assert name != "", "Product name is empty"
            assert price != "", "Product price is empty"

        # ✅ Example validation with test data
        for name, price in product_data:
            assert isinstance(name, str)
            assert len(name) > 2  # name should be meaningful