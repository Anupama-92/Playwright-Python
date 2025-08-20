
from playwright.sync_api import Page


class MicrosoftLoginPage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.user_name = self.page.get_by_role("textbox", name="Enter your email, phone, or")
        self.next_button = self.page.get_by_role("button", name="Next")
        self.password_input = self.page.get_by_role("textbox", name="Enter the password for chorus")
        self.signin_button = self.page.get_by_role("button", name="Sign in")
        self.yes_button = self.page.get_by_role("button", name="Yes")

    def navigate_to_login(self):
        self.page.goto(self.base_url)

    def enter_username(self, username: str):
        self.user_name.click()
        self.user_name.fill(username)
        self.next_button.click()

    def enter_password(self, password: str):
        self.password_input.click()
        self.password_input.fill(password)
        self.signin_button.click()

    def confirm_stay_signed_in(self):
        self.yes_button.click()

