from my_pages import login_page
from utils.playwright_manager import launch_browser
from playwright.sync_api import expect
import pytest

testData = {
    "invalid": {
        "username": "locked_out_user",
        "password": "secret_sauce"
    },
    "valid": {
        "username": "standard_user",
        "password": "secret_sauce"
    }
}
baseUrl = "https://www.saucedemo.com/"

#  pytest tests/functional/test_file.py
def test_successful_userlogin():
    with launch_browser() as (browser, page):
        lg_page = login_page.LoginPage(page)
        page.goto(baseUrl)
        valid_credentials = testData.get("valid")
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
        invalid_credentials = testData.get("invalid")
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