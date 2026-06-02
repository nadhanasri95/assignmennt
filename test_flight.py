import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time


class TestFlightTicket:

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

        assert "Expedia" in driver.title
        print("✅ Site opened successfully")


    def test_booking(self,driver):
        driver.get("https://www.expedia.com/")
        wait = WebDriverWait(driver, 2)

        flight = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Flights']"))
        )

        flight.click()
        #verify page content
        wait = WebDriverWait(driver, 15)
        roundtrip = wait.until(
            EC.presence_of_element_located((
                By.XPATH, "//span[text()='roundtrip']"))
        )
        assert roundtrip.is_displayed()
        time.sleep(10)
        text_search=self.driver.find_element(By.NAME, "destination_select")
        time.sleep(2)
        text_search.send_keys("Abudhabi")
        time.sleep(2)
        text_search.send_keys(Keys.ENTER)
        calender = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='Sun']"))
        )
        time.sleep(2)
        assert calender.is_displayed()
        logging.info("working as expected")
        time.sleep(2)
        date_10 = wait.until(
            EC.element_to_be_clickable((By.XPATH,"//div[@role='button'].//div[text()='10']]"))
        )
        time.sleep(2)
        date_10.click()
        done=wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@date-stid='apply-date-selector']"))
        )
        done.click()
        search_button = wait.until(
            EC.element_to_be_clickable((By.ID,"search_button"))
        )
        search_button.click()
        time.sleep(2)
        assert "flights" in driver.title
        logging.info("testing is completed")
        time.sleep(2)


