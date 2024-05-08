from site_pages.base_page import BasePage
from playwright.sync_api import Page

class InventoryPage(BasePage):
    def __init__(self, page: Page):
        self.page = page

    def get_quantity_text(self):
        OnesireText = self.page.locator("#cart_contents_container > div > div.cart_list > div.cart_item > div.cart_quantity")
        return OnesireText
    
    def get_price_text(self):
        OnesireText = self.page.locator("#cart_contents_container > div > div.cart_list > div.cart_item > div.cart_item_label > div.item_pricebar > div")
        return OnesireText
    
    def click_add_checkout(self):
        self.page.locator("#checkout").click()
