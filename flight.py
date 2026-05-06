import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestExpedia:

    @pytest.fixture
    def driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")

        driver = webdriver.Chrome(options=options)
        yield driver
        driver.quit()

    # ✅ Test 1 - Open Site
    def test_open_site(self, driver):
        driver.get("https://www.expedia.com/")
        time.sleep(6)

        assert "Expedia" in driver.page_source
        print("✅ Site opened successfully")

    # ✅ Test 2 - Flight Booking
    def test_flight_booking(self, driver):
        driver.get("https://www.expedia.com/")
        wait = WebDriverWait(driver, 25)

        # 🔹 Flights tab (FIXED locator)
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@aria-controls='search_form_product_selector_flights']")
        )).click()

        # 🔹 FROM (Kannur)
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@aria-label='Leaving from']")
        )).click()

        from_input = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@id='origin_select']")
        ))
        from_input.send_keys("Kannur")
        time.sleep(25)
        from_input.send_keys(Keys.ENTER)

        # 🔹 TO (Abu Dhabi)
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@aria-label='Going to']")
        )).click()

        to_input = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@id='destination_select']")
        ))
        to_input.send_keys("Abu Dhabi")
        time.sleep(25)
        to_input.send_keys(Keys.ENTER)

        # 🔹 DATE
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@aria-label='Departing']")
        )).click()

        # select any 2 dates
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//button[@data-day])[10]")
        )).click()

        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//button[@data-day])[15]")
        )).click()

        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@data-stid='apply-date-picker']")
        )).click()

        # 🔹 SEARCH (blue button)
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit']")
        )).click()

        time.sleep(25)

        # ✅ Validation
        assert "flight" in driver.current_url.lower()
        print("✅ Flight search successful")