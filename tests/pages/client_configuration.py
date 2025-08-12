class ClientConfigurationPage:
    def __init__(self, page):
        self.page = page
        self.home_frame = self.page.frame_locator("#applicationId")

    def navigate_to_project_management(self):
        self.page.get_by_role("img", name="Project Management").click()

    def navigate_to_client_configuration(self):
        self.page.pause()
        self.home_frame.locator("img.menuicon[src='assets/configuration.png']").hover()
        self.home_frame.get_by_text("Client Configuration").click()

    def add_new_client(self, client_name: str, address: str, city: str, state: str):
        self.home_frame.get_by_role("button", name="Add Client").click()
        self.home_frame.get_by_role("textbox", name="Enter Client Name").fill(client_name)
        self.home_frame.get_by_role("combobox", name="Search Region").click()
        self.home_frame.get_by_role("option", name="south").click()
        self.home_frame.get_by_role("combobox", name="Search Country").click()
        self.home_frame.get_by_role("option", name="India").click()
        self.home_frame.get_by_role("textbox", name="Enter Address").fill(address)
        self.home_frame.get_by_role("textbox", name="Enter City").fill(city)
        self.home_frame.get_by_role("textbox", name="Enter State").fill(state)
        self.home_frame.get_by_role("button", name="Add", exact=True).click()
        self.home_frame.get_by_role("alert", name="Client details added successfully").is_visible()




