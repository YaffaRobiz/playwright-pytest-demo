from playwright.sync_api import Page

class HamburgerMenu:
    def __init__(self, page: Page):
        self.page = page
        self.menu_button = page.get_by_role("button", name="Open Menu")
        self.all_items_link = page.get_by_role("link", name="All Items")
        self.about_link = page.get_by_role("link", name="About")
        self.logout_link = page.get_by_role("link", name="Logout")
        self.reset_app_state_link = page.get_by_role("link", name="Reset App State")
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
    
    


    
