from site_pages.base_page import BasePage
from playwright.sync_api import Page

class InventoryPage(BasePage):
    def __init__(self, page: Page):
        self.page = page

    def get_onesie_text(self):
        product_selector = "#item_2_title_link > div"
        product_elements = self.page.locator(product_selector)
        return product_elements
    
    def add_fleece_jacket_tocart(self):
        self.page.locator("[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]").click()
    
    def navigate_to_cart(self):
        self.page.locator("[data-test=\"shopping-cart-link\"]").click()
    

