import pytest

from tests.dataclass import ChorusDomains
from tests.utils.browser_utils import BrowserManager
from tests.pages.microsoft_login_page import MicrosoftLoginPage
from tests.config.config import Config



@pytest.mark.e2e
def test_microsoft_login(domains: ChorusDomains):
    browser = BrowserManager()
    page = browser.launch_browser()

    login_page = MicrosoftLoginPage(page, domains.chorus_fe_url)
    login_page.navigate_to_login()
    login_page.enter_username(Config.USERNAME)
    login_page.enter_password(Config.PASSWORD)
    login_page.confirm_stay_signed_in()

    browser.close_browser()
