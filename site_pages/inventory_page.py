from site_pages.base_page import BasePage
from playwright.sync_api import Page

class InventoryPage(BasePage):
    def __init__(self, page: Page):
        self.page = page

    def get_onesie_text(self):
        product_selector = "#item_2_title_link > div"
        product_elements = self.page.locator(product_selector)
        return product_elements
    
    def click_add_to_cart(self):
        self.page.locator("#add-to-cart-sauce-labs-onesie").click()
