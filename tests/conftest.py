import os
import pytest

from dotenv import load_dotenv

from drivers import chrome_driver
from my_store import MyStore

load_dotenv(override=True)


@pytest.fixture()
def my_store():
    driver = chrome_driver()
    store = MyStore(driver=driver)
    yield store
    if os.environ.get("CLOSE_BROWSER") == "true":
        driver.quit()
