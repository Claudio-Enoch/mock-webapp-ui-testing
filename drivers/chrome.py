from selenium.webdriver import Chrome, ChromeOptions


def chrome_driver():
    options = ChromeOptions()
    options.add_experimental_option("detach", True)  # allow the driver to stay open for debug
    driver = Chrome(options=options)
    driver.implicitly_wait(15)
    return driver
