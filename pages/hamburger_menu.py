from playwright.sync_api import Page

class HamburgerMenu:
    def __init__(self, page: Page):
        self.page = page
        self.menu_button = page.get_by_role("button", name="Open Menu")
        self.all_items_link = page.locator("[data-test=\"inventory-sidebar-link\"]")
        self.about_link = page.locator("[data-test=\"about-sidebar-link\"]")
        self.logout_link = page.locator("[data-test=\"logout-sidebar-link\"]")
        self.reset_app_state_link = page.locator("[data-test=\"reset-sidebar-link\"]")
        self.close_menu_button = page.get_by_role("button", name="Close Menu")
   

    def open_menu(self):
        self.menu_button.click()

    def navigate_to_all_items(self):
        self.all_items_link.click() 

    def navigate_to_about(self):
        self.about_link.click() 
    
    def logout(self):
        self.logout_link.click()

    def reset_app_state(self):
        self.reset_app_state_link.click()

    def close_menu(self):
        self.close_menu_button.click()
    
    


    
