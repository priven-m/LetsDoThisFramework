from page_objects import base_page, home_page, login_page
from utils.playwright_manager import launch_browser
from playwright.sync_api import expect
import pytest

testData = [{
                "Camera": "Canon EOS 5D",
                "CameraPageTitle": "Search - Canon EOS 5D",
                "Phone": "Iphone"
            },
            {
                "username":"mnicedevelopment@gmail.com",
                "password":"pass123"
            }
    ]

#  pytest tests/functional/test_sample.py
@pytest.mark.parametrize("test_data", testData)
def test_userlogin_and_userprofile(test_data):
    with launch_browser() as browser:
        page = browser.new_page()
        hpage = home_page.HomePage(page)
        lpage = login_page.LoginPage(page)
        page.goto("https://awesomeqa.com/ui/")

        username = test_data["username"]
        password = test_data["password"]

        page.click('text=Login')

        page.fill('#username', username)
        page.fill('#password', password)

        # Click the "Login" button
        page.click('#login-button')

        # Verify that the user is redirected to the dashboard
        assert page.title() == 'Awesome QA - Dashboard'

        # Navigate to the user profile
        page.click('text=Profile')

        # Verify that the user's profile information is displayed
        assert page.inner_text('.user-profile') == 'User Profile: Your Username'

        page.click('text=Logout')

        # Verify that the user is redirected to the home page after logout
        assert page.title() == 'Awesome QA - Home'

@pytest.mark.parametrize("test_data", testData)
def test_product_search_functionality(test_data):
    with launch_browser() as browser:
        page = browser.new_page()
        your_page = home_page.HomePage(page)
        page.goto("https://awesomeqa.com/ui/")
        your_page.search_canon_camera_from_homePage(test_data["Camera"])
        assert page.title() == test_data["CameraPageTitle"]