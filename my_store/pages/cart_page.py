from time import sleep
from urllib.parse import urlparse, parse_qs

from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.remote.webelement import WebElement


class CartPage:

    def __init__(self, driver: RemoteWebDriver):
        self._driver = driver

    def get_products(self) -> dict:
        products = self._driver.find_elements_by_css_selector("tr.cart_item")
        products_dict = {}
        for product in products:
            product_id = self._get_product_id(product=product)
            product_name = product.find_element_by_css_selector("p.product-name>a").text
            product_price = float(product.find_element_by_css_selector("span.price").text[1:])
            product_url = product.find_element_by_css_selector("td.cart_product>a").get_attribute("href")
            color = product_url.split("color-")[-1]
            quantity = int(product.find_element_by_css_selector("input.cart_quantity_input").get_attribute("value"))
            products_dict[product_id] = dict(name=product_name, price=product_price, color=color, quantity=quantity)
        return products_dict

    def delete_product(self, product_id: str):
        products = self._driver.find_elements_by_css_selector("tr.cart_item")
        product = [product for product in products if product_id == self._get_product_id(product)][0]
        product.find_element_by_css_selector("a.cart_quantity_delete").click()
        sleep(3)  # deletion is a slow fade  ToDo: add explicit wait on element being no longer visible

    @staticmethod
    def _get_product_id(product: WebElement) -> str:
        product_url = product.find_element_by_css_selector("td.cart_product>a").get_attribute("href")
        product_id = parse_qs(urlparse(url=product_url).query)["id_product"][0]
        return product_id
