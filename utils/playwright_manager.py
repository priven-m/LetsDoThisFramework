from playwright.sync_api import sync_playwright
from contextlib import contextmanager

@contextmanager
def launch_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield browser
        browser.close()
        