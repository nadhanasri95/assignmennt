import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import logging

class TestGoogle:
    @pytest.fixture
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://google.com/")
        yield
        logging.info("testing is completed")
        self.driver.quit()

    def test_should_open_google_and_verify_title(self, setup):
        assert self.driver.title == "Google"

    def test_should_search_a_query(self, setup):


        search_textarea= self.driver.find_element(By.NAME,"q")
        search_textarea.send_keys("selenium")
        search_textarea.send_keys(Keys.ENTER)
        time.sleep(3)
        assert "selenium" in self.driver.title


