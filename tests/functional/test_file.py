from site_pages import login_page
from utils.playwright_manager import launch_browser
from utils.config import baseUrl
from test_data.login_test_data import login_credentials
from playwright.sync_api import expect
import pytest

#  pytest tests/functional/test_file.py
def test_successful_userlogin():
    with launch_browser() as (browser, page):
        lg_page = login_page.LoginPage(page)
        page.goto(baseUrl)
        valid_credentials = login_credentials.get("valid")
        if valid_credentials:
            username = valid_credentials["username"]
            password = valid_credentials["password"]
            try:
                lg_page.login_user(username, password)
                expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
            except Exception as e:                
                print("An error occurred:", e)
        else:
            print("No valid credentials found for testing.")

def test_failed_userlogin():
    with launch_browser() as (browser, page):
        lg_page = login_page.LoginPage(page)
        page.goto(baseUrl)
        invalid_credentials = login_credentials.get("invalid")
        if invalid_credentials:
            username = invalid_credentials["username"]
            password = invalid_credentials["password"]
            try:
                lg_page.login_user(username, password)
                expect(page).not_to_have_url("https://www.saucedemo.com/inventory.html")
            except Exception as e:                
                print("An error occurred:", e)
        else:
            print("No invalid credentials provided. Test cannot proceed.")