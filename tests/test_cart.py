import pytest
from utils.config import Config
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.regression
def test_add_product_to_cart(page):
    login_page = LoginPage(page)
    login_page.navigate(Config.BASE_URL)
    login_page.login(Config.USERNAME, Config.PASSWORD)

    inventory_page = InventoryPage(page)
    inventory_page.add_product_to_cart()

    assert inventory_page.get_cart_count() == "1"
