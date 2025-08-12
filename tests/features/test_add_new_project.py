from tests.dataclass import ChorusDomains
from tests.utils.browser_utils import BrowserManager
from tests.pages.microsoft_login_page import MicrosoftLoginPage
from tests.pages.client_configuration import ClientConfigurationPage
from tests.pages.project_configuration import ProjectConfigurationPage
from tests.config.config import Config


def test_add_project_details(domains: ChorusDomains):
    browser = BrowserManager()
    page = browser.launch_browser()

    login_page = MicrosoftLoginPage(page, domains.chorus_fe_url)
    login_page.navigate_to_login()
    login_page.enter_username(Config.USERNAME)
    login_page.enter_password(Config.PASSWORD)
    login_page.confirm_stay_signed_in()
    home_page = ClientConfigurationPage(page)
    home_page.navigate_to_project_management()
    pconfig_page = ProjectConfigurationPage(page)
    pconfig_page.navigate_to_project_configuration()
    pconfig_page.add_new_project(Config.PROJECT_NAME, Config.DESCRIPTION, Config.START_DATE, Config.HOURS_PER_DAY,
                                 Config.ALIAS_EMAIL, Config.TECH_STACK_TO_SELECT)
    pconfig_page.upload_file()
    pconfig_page.add_project()

    browser.close_browser()