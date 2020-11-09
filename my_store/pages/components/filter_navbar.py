from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver


class FilterNavbar:

    def __init__(self, driver: RemoteWebDriver):
        self._driver = driver

    def get_categories(self) -> dict:
        """Return a dict of category_name:count"""
        categories = self._driver.find_elements_by_css_selector("ul#ul_layered_category_0>li")
        category_dict = {}
        for category in categories:
            item, count = category.text.split(" (")  # ToDo: replace with regex
            item = item.strip()
            count = count.split(")")[0]
            category_dict[item] = count
        return category_dict
