from itertools import product
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
    
    
    def add_item_to_cart(self, item_name: str):
        product = self.page.locator(
            ".inventory_item",
            has=self.page.locator(".inventory_item_name", has_text=item_name)
            )
        product.locator("button").click()

    def add_items_to_cart(self, item_names: list[str]):
        for item_name in item_names:
            self.add_item_to_cart(item_name)

    def remove_item_from_cart(self, item_name: str):
        product = self.page.locator(
            ".inventory_item",
            has=self.page.locator(".inventory_item_name", has_text=item_name)
            )
        product.locator("button").click()

    def remove_items_from_cart(self, item_names: list[str]):
        for item_name in item_names:
            self.remove_item_from_cart(item_name)

    def go_to_cart(self):
        self.cart_link.click()
    
    
    