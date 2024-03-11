import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class MyTest(unittest.TestCase):
    def setUp(self):
        self.SEARCH_INPUT = '//input[@id="search"]'
        self.url = "https://www.youtube.com/"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_youtube_search(self):
        driver = self.driver
        driver.get(self.url)

        # Find the search input field and enter a search query
        search_input = driver.find_element(By.XPATH, self.SEARCH_INPUT)
        search_query = "sss"
        search_input.send_keys(search_query)
        search_input.send_keys(Keys.RETURN)

        # Wait for the search results page to load
        time.sleep(2)

        # Assert that the title of the page contains the search query
        self.assertIn(search_query, driver.title)


if __name__ == "__main__":
    unittest.main()
