from playwright.sync_api import sync_playwright
from contextlib import contextmanager

@contextmanager
def launch_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=2000)
        context = browser.new_context()
        page = context.new_page()
        try:
            yield browser, page
        finally:
            browser.close()
        