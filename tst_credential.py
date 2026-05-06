import time


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
#
#
#
class TestLogin:

    user_credentials = [
        ("user1@gmail.com", "password1"),
        ("user2@gmail.com", "password2"),
        ("hansa@gmail.com", "hansa123")
    ]

    @pytest.fixture
    def driver(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demo.spreecommerce.org")

        time.sleep(5)
        yield self.driver
        self.driver.quit()

    @pytest.mark.parametrize("email, password", user_credentials)
    def test_login(self, driver, email, password):
        print(email, password)

        driver.get("https://demo.spreecommerce.org/account")
        time.sleep(5)
        driver.implicitly_wait(5)

        email_element = driver.find_element(By.ID, "email")
        password_element = driver.find_element(By.ID, "password")

        email_element.send_keys(email)

        password_element.send_keys(password)


        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

        time.sleep(3)

        actual_text = driver.find_element(
        By.CSS_SELECTOR, ".text-2xl.font-bold.text-gray-900.mb-6").get_attribute("innerHTML")

        print(actual_text)

        assert actual_text == "Account Overview"