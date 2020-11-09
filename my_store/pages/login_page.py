from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver


class LoginPage:
    def __init__(self, driver: RemoteWebDriver):
        self._driver = driver

    @property
    def alert_message(self) -> str:
        return self._driver.find_element_by_css_selector("div.alert").text

    def log_in(self, username="wejoolpeblmtunsiex@wqcefp.online", password="password"):
        self._driver.find_element_by_id("email").send_keys(username)
        self._driver.find_element_by_id("passwd").send_keys(password)
        self._driver.find_element_by_id("SubmitLogin").click()
