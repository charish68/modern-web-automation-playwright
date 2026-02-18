from playwright.sync_api import Page

class InventoryPage:

    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_button = page.locator("button[data-test='add-to-cart-sauce-labs-backpack']")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def add_product_to_cart(self):
        self.add_to_cart_button.click()

    def get_cart_count(self):
        return self.cart_badge.text_content()
