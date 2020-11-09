from typing import List
from urllib.parse import urlparse, parse_qs

from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.remote.webelement import WebElement


class ProductContent:

    def __init__(self, driver: RemoteWebDriver):
        self._driver = driver

    def get_search_count(self) -> int:
        """Parse the search results banner for total results"""
        count = self._driver.find_element_by_css_selector("span.heading-counter").text
        return int(count.split()[0])

    def get_products(self, product_view: str = "grid") -> dict:
        """Get a dict of items based on product_view: grid | list"""
        self._driver.find_element_by_css_selector(f"#{product_view}>a").click()
        products = self._driver.find_elements_by_css_selector("ul.product_list > li")
        products_dict = self._parse_products(products=products)
        return products_dict

    def add_product_to_cart(self, product_id: str):
        """Add product to cart and click continue shopping"""
        self._driver.find_element_by_css_selector(f"div.button-container>a[data-id-product='{product_id}']").click()
        self._driver.find_element_by_css_selector("span[title='Continue shopping']").click()

    def preview_product(self, product_id: str) -> dict:
        """
        Select a product, by product_id, to preview and return a dictionary of properties from its <iframe> modal
        {'price': 16.51, 'colors': ['red', 'blue'], 'name': 'Blouse' }
        """
        products = self._driver.find_elements_by_css_selector("ul.product_list > li")

        # get product <li> by product_id
        product = [product for product in products if self._parse_product_id(product) == product_id][0]

        product.find_element_by_css_selector("i.icon-eye-open").click()
        self._driver.switch_to.frame(frame_reference=self._driver.find_element_by_css_selector("iframe"))
        price = self._driver.find_element_by_css_selector("span#our_price_display").get_attribute("innerHTML")[1:]
        colors = [color.get_attribute("name").lower() for color in
                  self._driver.find_elements_by_css_selector("li>a.color_pick")]
        name = self._driver.find_element_by_css_selector("h1[itemprop='name']").text
        return dict(price=float(price), colors=colors, name=name)

    @staticmethod
    def _parse_products(products: List[WebElement]) -> dict:
        """
        Take in an <ul> of items and return a dictionary of product_ids and corresponding properties
        {
            '1': {'price': 16.51, 'colors': ['red', 'blue'], 'name': 'Blouse' },
            '2': {'price': 16.51, 'colors': ['orange'], 'name': 'Dress' }
        }
        """
        products_dict = {}
        for product in products:
            product_id = ProductContent._parse_product_id(web_element=product)
            price = product.find_element_by_css_selector("span.product-price").get_attribute("innerHTML").strip()[1:]
            colors = [color.get_attribute("href").split("color-")[-1] for color in
                      product.find_elements_by_css_selector("li>a.color_pick")]
            name = product.find_element_by_css_selector("a.product-name").text
            products_dict[product_id] = dict(price=float(price), colors=colors, name=name)
        return products_dict

    @staticmethod
    def _parse_product_id(web_element: WebElement) -> str:
        """Given a product WebElement, return the product's ID"""
        url = web_element.find_element_by_css_selector("a.quick-view").get_attribute("href")
        product_id = parse_qs(urlparse(url=url).query)["id_product"][0]
        return product_id
