from playwright.sync_api import sync_playwright
from tests.config.config import Config


class BrowserManager:
    def __init__(self, headless: bool = Config.HEADLESS):
        self.headless = headless
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    def launch_browser(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=self.headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        return self.page

    def close_browser(self):
        self.context.close()
        self.browser.close()
        self.playwright.stop()
