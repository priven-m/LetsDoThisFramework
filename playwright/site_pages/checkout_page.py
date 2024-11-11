from site_pages.base_page import BasePage
from playwright.sync_api import Page

class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        self.page = page    
    
    def enter_name_for_checkout(self, firstName):
        self.page.locator("[data-test=\"firstName\"]").fill(firstName)
    
    def enter_lastName_for_checkout(self, lastName):
        self.page.locator("[data-test=\"lastName\"]").fill(lastName)

    def enter_postalCode_for_checkout(self, postalCode):
        self.page.locator("[data-test=\"postalCode\"]").fill(postalCode)

    def click_continue(self):
        self.page.locator("[data-test=\"continue\"]").click()