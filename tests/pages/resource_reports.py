import os

from playwright.sync_api import Page


class ResourceReportsPage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.home_frame = self.page.frame_locator("#applicationId")
        self.pmo_icon = self.page.get_by_role("img", name="Project Management")
        self.resource_reports = self.home_frame.locator("img.menuicon[src='assets/resource-reports.png']")
        self.export_report_button = self.home_frame.get_by_role("button", name="Export Reports")

    def navigate_to_resource_reports(self):
        self.pmo_icon.click()
        self.resource_reports.click()

    def export_report(self, download_dir: str):
        with self.page.expect_download() as download_info:
            self.export_report_button.click()

        download = download_info.value
        file_path = os.path.join(download_dir, download.suggested_filename)
        download.save_as(file_path)
        print(f"File downloaded to: {file_path}")
        return file_path

