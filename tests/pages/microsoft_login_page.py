
from playwright.sync_api import Page


class MicrosoftLoginPage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    def navigate_to_login(self):
        self.page.goto(self.base_url)

    def enter_username(self, username: str):
        self.page.get_by_role("textbox", name="Enter your email, phone, or").click()
        self.page.get_by_role("textbox", name="Enter your email, phone, or").fill(username)
        self.page.get_by_role("button", name="Next").click()

    def enter_password(self, password: str):
        self.page.get_by_role("textbox", name="Enter the password for chorus").click()
        self.page.get_by_role("textbox", name="Enter the password for chorus").fill(password)
        self.page.get_by_role("button", name="Sign in").click()

    def confirm_stay_signed_in(self):
        self.page.get_by_role("button", name="Yes").click()
        self.page.pause()
