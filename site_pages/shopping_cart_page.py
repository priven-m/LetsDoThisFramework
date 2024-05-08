from site_pages.base_page import BasePage
from playwright.sync_api import Page

class ShoppingPage(BasePage):
    def __init__(self, page: Page):
        self.page = page
  
    def get_price_text(self):
        get_unitprice = self.page.locator("[data-test=\"inventory-item-price\"]")
        return get_unitprice
    
    def get_quantity_in_cart(self):
        get_quantity = self.page.locator("[data-test=\"item-quantity\"]")
        return get_quantity

    def checkout_product(self):
        self.page.locator("[data-test=\"checkout\"]").click()