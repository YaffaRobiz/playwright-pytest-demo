from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        # self.product_titles_selector = page.locator(".inventory_item_name")
        self.product_titles = page.locator(".inventory_item_name").all_inner_texts()
        self.add_to_cart_buttons = page.locator("button[data-test^='add-to-cart-']")
        self.cart_button = page.locator(".shopping_cart_link")


    def get_product_titles(self):
        return self.product_titles 
    
    def go_to_cart(self):
        self.cart_button.click()