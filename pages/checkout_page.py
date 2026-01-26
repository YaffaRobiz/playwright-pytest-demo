from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = page.get_by_placeholder("First Name")
        self.last_name_input = page.get_by_placeholder("Last Name")
        self.postal_code_input = page.get_by_placeholder("Postal Code")
        self.continue_button = page.get_by_role("button", name="Continue")
        self.cancel_button = page.get_by_role("button", name="Cancel")
        self.finish_button = page.get_by_role("button", name="Finish")


    def fill_checkout_information(self, first_name: str, last_name: str, postal_code: str):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)    