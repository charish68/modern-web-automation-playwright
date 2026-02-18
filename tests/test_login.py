import pytest
from utils.config import Config
from pages.login_page import LoginPage

@pytest.mark.smoke
def test_successful_login(page):
    login_page = LoginPage(page)
    login_page.navigate(Config.BASE_URL)
    login_page.login(Config.USERNAME, Config.PASSWORD)

    assert page.url == "https://www.saucedemo.com/inventory.html"
