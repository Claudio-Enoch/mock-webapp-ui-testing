from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver


class Navbar:

    def __init__(self, driver: RemoteWebDriver):
        self._driver = driver

    def click_contact_us(self):
        self._driver.find_element_by_css_selector("div#contact-link>a").click()

    def click_sign_in(self):
        self._driver.find_element_by_css_selector("div.header_user_info>a").click()
