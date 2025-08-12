from playwright.sync_api import Page


class ClientConfigurationPage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.home_frame = self.page.frame_locator("#applicationId")
        self.pmo_icon = self.page.get_by_role("img", name="Project Management")
        self.left_panel_expand = self.home_frame.locator("img.menuicon[src='assets/configuration.png']")
        self.client_configuration = self.home_frame.get_by_text("Client Configuration")
        self.add_client_button = self.home_frame.get_by_role("button", name="Add Client")
        self.client_name = self.home_frame.get_by_role("textbox", name="Enter Client Name")
        self.search_region = self.home_frame.get_by_role("combobox", name="Search Region")
        self.region_option = self.home_frame.get_by_role("option", name="south")
        self.search_country = self.home_frame.get_by_role("combobox", name="Search Country")
        self.country_option = self.home_frame.get_by_role("option", name="India")
        self.address = self.home_frame.get_by_role("textbox", name="Enter Address")
        self.city = self.home_frame.get_by_role("textbox", name="Enter City")
        self.state = self.home_frame.get_by_role("textbox", name="Enter State")
        self.add_button = self.home_frame.get_by_role("button", name="Add", exact=True)
        self.success_message = self.home_frame.get_by_role("alert", name="Client details added successfully")

    def navigate_to_project_management(self):
        self.pmo_icon.click()

    def navigate_to_client_configuration(self):
        self.left_panel_expand.hover()
        self.client_configuration.click()

    def add_new_client(self, client_name: str, address: str, city: str, state: str):
        self.add_client_button.click()
        self.client_name.fill(client_name)
        self.search_region.click()
        self.region_option.click()
        self.search_country.click()
        self.country_option.click()
        self.address.fill(address)
        self.city.fill(city)
        self.state.fill(state)
        self.add_button.click()
        self.success_message.is_visible()




