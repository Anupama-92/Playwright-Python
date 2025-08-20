import os

import pytest
from playwright.sync_api import sync_playwright

from tests.config.config import Config
from tests.dataclass import ChorusDomains
from tests.pages.client_configuration import ClientConfigurationPage
from tests.utils.browser_utils import BrowserManager
from tests.pages.microsoft_login_page import MicrosoftLoginPage
from tests.pages.resource_reports import ResourceReportsPage
from tests.utils.excel_utils import read_and_format_excel
from tests.utils.ui_utils import read_ui_grid_data


@pytest.mark.e2e
def test_resource_report(domains: ChorusDomains, tmp_path):
    # Launch browser
    browser = BrowserManager()
    page = browser.launch_browser()

    # Step 1: Login
    login_page = MicrosoftLoginPage(page, domains.chorus_fe_url)
    login_page.navigate_to_login()
    login_page.enter_username(Config.USERNAME)
    login_page.enter_password(Config.PASSWORD)
    login_page.confirm_stay_signed_in()

    # Step 2: Navigate to Resource Reports and Export
    reports_page = ResourceReportsPage(page, domains.chorus_fe_url)
    reports_page.navigate_to_resource_reports()
    download_dir = str(tmp_path)   # pytest tmp dir for downloads
    excel_file_path = reports_page.export_report(download_dir)

    # Step 3: Read Excel Data
    excel_data = read_and_format_excel(excel_file_path)

    # Step 4: Read UI Grid Data (with pagination)
    ui_data = read_ui_grid_data(page)

    # Step 5: Assertions
    assert len(excel_data) == len(ui_data), (
        f"Row count mismatch: Excel={len(excel_data)}, UI={len(ui_data)}"
    )

    for i, (excel_row, ui_row) in enumerate(zip(excel_data, ui_data), start=1):
        assert excel_row == ui_row, f"Row {i} mismatch:\nExcel: {excel_row}\nUI: {ui_row}"

    print("Excel data matches UI grid data")
