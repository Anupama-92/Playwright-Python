import re


class ProjectConfigurationPage:
    def __init__(self, page):
        self.page = page
        self.home_frame = self.page.frame_locator("#applicationId")

    def navigate_to_project_configuration(self):
        self.page.pause()
        self.home_frame.locator("img.menuicon[src='assets/configuration.png']").hover()
        self.home_frame.get_by_text("Project Configuration").click()

    def add_new_project(self, project_name: str, description: str, start_date: str,hours_per_day: str, alias_email: str,
                        tech_stack_to_select: str):
        self.page.pause()
        self.home_frame.get_by_role("button", name="Add Project").click()
        self.home_frame.get_by_role("combobox", name="Search Client").click()
        self.home_frame.get_by_role("option", name="AutomationTest1").click()
        self.home_frame.get_by_role("textbox", name="Enter Project Name").fill(project_name)
        self.home_frame.get_by_role("textbox", name="Enter Description").fill(description)
        self.home_frame.get_by_role("textbox", name="Select Start Date").fill(start_date)
        self.home_frame.get_by_role("textbox", name="Enter Hours Per Day").fill(hours_per_day)
        self.home_frame.get_by_role("textbox", name="Enter Email").fill(alias_email)
        self.home_frame.locator("//div[@class='c-btn' and .//span[text()='Select Technologies']]").click()
        for tech in tech_stack_to_select:
            checkbox = self.home_frame.locator("ul.lazyContainer li.pure-checkbox label.ng-star-inserted",
                               has_text=re.compile(f"^{re.escape(tech)}$"))
            checkbox.click()

    def upload_file(self):
        self.home_frame.locator("#fileInput").set_input_files(r"D:\Personal\Playwright-Python\tests\config\test.txt")

    def add_project(self):
        self.home_frame.get_by_role("button", name="Add", exact=True).click()
        self.home_frame.get_by_role("alert", name="Project details added successfully").is_visible()



