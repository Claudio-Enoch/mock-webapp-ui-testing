from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver


class Navbar:

    def __init__(self, driver: RemoteWebDriver):
        self._driver = driver

    def search(self, search_query: str):
        self._driver.find_element_by_id("search_query_top").send_keys(search_query)
        self._driver.find_element_by_css_selector("button.button-search").click()

    def click_cart(self):
        self._driver.find_element_by_css_selector("div.shopping_cart>a").click()

    def click_contact_us(self):
        self._driver.find_element_by_css_selector("div#contact-link>a").click()

    def click_sign_in(self):
        self._driver.find_element_by_css_selector("div.header_user_info>a").click()

    def click_sign_out(self):
        self._driver.find_element_by_css_selector("a.logout").click()

    def click_category_women(self):
        self._driver.find_element_by_css_selector("a[title='Women']").click()

    def click_category_dresses(self):
        self._driver.find_element_by_css_selector("a[title='Dresses']").click()

    def click_category_t_shirts(self):
        self._driver.find_element_by_css_selector("a[title='T-shirts']").click()
