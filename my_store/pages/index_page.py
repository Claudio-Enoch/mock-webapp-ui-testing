from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

from my_store.pages.navbar import Navbar


class IndexPage:

    def __init__(self, driver: RemoteWebDriver):
        self._driver = driver
        self.navbar = Navbar(driver=self._driver)
