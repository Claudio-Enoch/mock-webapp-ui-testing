from my_store.pages import *
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver


class MyStore:

    def __init__(self, driver: RemoteWebDriver, url="http://automationpractice.com"):
        self._driver = driver
        self._driver.get(url=url)

    @property
    def index_page(self):
        return IndexPage(driver=self._driver)

    @property
    def login_page(self):
        return LoginPage(driver=self._driver)

    @property
    def cart_page(self):
        return CartPage(driver=self._driver)

    @property
    def url(self):
        return self._driver.current_url

