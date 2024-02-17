from page_objects.base_page import BasePage
from playwright.sync_api import Page

class HomePage(BasePage):
    def __init__(self, page: Page):
        self.page = page

    '''def navigate_to_register_openCart_site(self):
        self.page.get_by_title("My Account").click()
        self.page.keyboard.press("Enter")'''
        
    '''def navigate_to_logout_openCart_site(self):
        self.page.get_by_title("My Account").click()
        self.page.keyboard.press("Enter")'''
    
    '''def navigate_to_my_account(self):
        self.page.get_by_title("My Account").click()
        self.page.keyboard.press("Enter")'''
    
    '''def navigate_to_my_wish_list(self):
        self.page.get_by_title("My Account").click()
        self.page.keyboard.press("Enter")''' 
    
    '''def navigate_to_my_shopping_cart(self):
        self.page.get_by_title("My Account").click()
        self.page.keyboard.press("Enter")'''  

    '''def navigate_to_checkout_page(self):
        self.page.get_by_title("My Account").click()
        self.page.keyboard.press("Enter")''' 
    
    def search_canon_camera_from_homePage(self, query):
        self.page.get_by_placeholder("Search").fill(query)
        self.page.keyboard.press("Enter")