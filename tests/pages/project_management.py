from tests.config.config import Config


class ProjectManagementPage:
    def __init__(self, page):
        self.page = page
        self.home_frame = self.page.frame_locator("#applicationId")

    def navigate_to_project_management(self):
        self.page.get_by_role("img", name="Project Management").click()

    def navigate_to_client_configuration(self):
        self.home_frame.get_by_role("tab", name="Client Configuration Client").click()

    def add_new_client(self):
        self.home_frame.get_by_role("button", name="Add Client").click()
        self.home_frame.get_by_role("textbox", name="Enter Client Name").click()


