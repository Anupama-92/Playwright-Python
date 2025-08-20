import pytest
import allure

from tests.dataclass import ChorusDomains
from tests.utils.browser_utils import BrowserManager
from tests.pages.microsoft_login_page import MicrosoftLoginPage
from tests.config.config import Config


@pytest.mark.e2e
@allure.feature("Authentication")
@allure.story("Microsoft Login")
@allure.title("Verify Microsoft login works successfully")
def test_microsoft_login(domains: ChorusDomains):
    browser = BrowserManager()
    page = browser.launch_browser()

    login_page = MicrosoftLoginPage(page, domains.chorus_fe_url)

    try:
        with allure.step("Navigate to Microsoft login page"):
            login_page.navigate_to_login()
            allure.attach(page.screenshot(), name="Login Page", attachment_type=allure.attachment_type.PNG)

        with allure.step("Enter username"):
            login_page.enter_username(Config.USERNAME)
            allure.attach(page.screenshot(), name="Entered Username", attachment_type=allure.attachment_type.PNG)

        with allure.step("Enter password"):
            login_page.enter_password(Config.PASSWORD)
            allure.attach(page.screenshot(), name="Entered Password", attachment_type=allure.attachment_type.PNG)

        with allure.step("Confirm stay signed in"):
            login_page.confirm_stay_signed_in()
            allure.attach(page.screenshot(), name="Stay Signed In", attachment_type=allure.attachment_type.PNG)

        with allure.step("Verify login success"):
            current_url = page.url
            page_title = page.title()

            allure.attach(current_url, name="Current URL", attachment_type=allure.attachment_type.TEXT)
            allure.attach(page_title, name="Page Title", attachment_type=allure.attachment_type.TEXT)

            assert "chorus" in current_url.lower(), "Login did not redirect to Chorus portal"

    finally:
        browser.close_browser()
