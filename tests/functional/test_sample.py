from page_objects import base_page, home_page, login_page
from utils.playwright_manager import launch_browser
from playwright.sync_api import expect

#  pytest tests/functional/test_sample.py
def test_product_search_functionality():
    with launch_browser() as browser:
        page = browser.new_page()
        your_page = home_page.HomePage(page)
        page.goto("https://awesomeqa.com/ui/")
        your_page.search_canon_camera_from_homePage("Canon EOS 5D")
        expect(page).to_have_title("Search - Canon EOS 5D")
        