from tests.dataclass import ChorusDomains
from tests.utils.browser_utils import BrowserManager
from tests.pages.microsoft_login_page import MicrosoftLoginPage
from tests.pages.client_configuration import ClientConfigurationPage
from tests.config.config import Config


def test_add_client_details(domains: ChorusDomains):
    browser = BrowserManager()
    page = browser.launch_browser()

    login_page = MicrosoftLoginPage(page, domains.chorus_fe_url)
    login_page.navigate_to_login()
    login_page.enter_username(Config.USERNAME)
    login_page.enter_password(Config.PASSWORD)
    login_page.confirm_stay_signed_in()
    PMO_page = ClientConfigurationPage(page, domains.chorus_fe_url)
    PMO_page.navigate_to_project_management()
    PMO_page.navigate_to_client_configuration()
    PMO_page.add_new_client(Config.CLIENT_NAME, Config.ADDRESS, Config.CITY, Config.STATE)

    browser.close_browser()
