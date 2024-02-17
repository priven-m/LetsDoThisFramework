from page_objects.base_page import BasePage
from playwright.sync_api import Page

class LoginPage(BasePage):
    def __init__(self, page: Page):
        self.page = page

    def click_login(self):
        self.page.get_by_role("link", name="Login").click()
    
    def enter_credentials(self, username, password):
        self.page.get_by_placeholder("E-Mail Address").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()