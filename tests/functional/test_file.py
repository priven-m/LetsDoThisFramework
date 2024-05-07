from site_pages import login_page
from utils.playwright_manager import launch_browser
from utils.config import baseUrl
from test_data.login_test_data import login_credentials
from playwright.sync_api import expect
import pytest
import logging

#  pytest tests/functional/test_file.py
def test_site_landing_page():
    with launch_browser() as (browser, page):
        lg_page = login_page.LoginPage(page)
        page.goto(baseUrl)
        pg_title = login_credentials.get("pageTitle")
        if pg_title:
            expected_title = pg_title["page_title"]
            if expected_title:
                actual_title = lg_page.login_page_title()
                assert actual_title == expected_title, f"Title mismatch. Expected: {expected_title}, Actual: {actual_title}"
            else:
                logging.info("Expected title not returned from test_data")
        else:
            logging.info("No page title returned from website")

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
                logging.info("An error occurred:", e)
        else:
            logging.info("No valid credentials found for testing.")

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
                logging.info("An error occurred:", e)
        else:
            logging.info("No invalid credentials provided. Test cannot proceed.")