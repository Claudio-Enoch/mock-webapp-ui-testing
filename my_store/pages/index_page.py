import time

from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from my_store.pages.components import Navbar, ProductContent, FilterNavbar


class IndexPage:

    def __init__(self, driver: RemoteWebDriver):
        self._driver = driver
        time.sleep(1)  # allow page components to fully load
        self.navbar = Navbar(driver=self._driver)
        self.filter_navbar = FilterNavbar(driver=self._driver)
        self.product_content = ProductContent(driver=self._driver)
