from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.item_name = page.locator("[data-test=\"inventory-item-name\"]")
        self.item_description = page.locator("[data-test=\"inventory-item-desc\"]")
        self.item_price = page.locator("[data-test=\"inventory-item-price\"]")
        self.add_to_cart_button = page.locator("[data-test^=\"add-to-cart-\"]")
        self.remove_item_button = page.locator("[data-test^=\"remove-\"]")
        self.cart_link = page.locator("[data-test=\"shopping-cart-link\"]")



    def get_all_item_names(self) -> list[str]:
        return self.item_name.all_inner_texts() 
    
    def count_items(self) -> int:
        return self.item_name.count()
    
    def get_all_item_prices(self) -> list[str]:
        return self.item_price.all_inner_texts()
    
    def add_item_to_cart(self, item_name: str):
        for i, name in enumerate(self.get_all_item_names()): # enumerate is a method that returns both the index and the value of each item in an iterable
            if name == item_name:
                self.add_to_cart_button.nth(i).click()
                break

    def remove_item_from_cart(self, item_name: str):
        for i, name in enumerate(self.get_all_item_names()): 
            if name == item_name:
                self.remove_item_button.nth(i).click()
                break

    def go_to_cart(self):
        self.cart_link.click()
    
    
    