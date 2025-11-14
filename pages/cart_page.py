from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator("[data-test=\"inventory-item\"]")
        self.checkout_button = page.locator("[data-test=\"checkout\"]")
        self.continue_shopping_button = page.locator("[data-test=\"continue-shopping\"]")
        self.remove_item_button = page.locator("[data-test^=\"remove-\"]")
        self.item_price = page.locator("[data-test=\"inventory-item-price\"]")
        self.item_name = page.locator("[data-test=\"inventory-item-name\"]")

    
    def click_continue_shopping_button(self):
        self.continue_shopping_button.click()

    def click_checkout_button(self):
        self.checkout_button.click()

    def get_cart_items_count(self) -> int:
        return self.cart_items.count()
    
    def get_cart_items_names(self) -> list[str]:
        return self.item_name.all_inner_texts()
    
    def get_cart_items_prices(self) -> list[str]:
        return self.item_price.all_inner_texts()
    
    def remove_item(self, item_name: str):
        for i, name in enumerate(self.get_cart_items_names()): # enumerate is a method that returns both the index and the value of each item in an iterable
            if name == item_name:
                self.remove_item_button.nth(i).click()
                break

    
    



    