from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator("[data-test=\"inventory-item\"]")
        self.checkout_button = page.get_by_role("button", name="Checkout")
        self.continue_shopping_button = page.get_by_role("button", name="Continue Shopping")
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
    
    def remove_item_from_cart(self, item_name: str):
        product = self.page.locator(
            ".cart_item",
            has=self.page.locator(".inventory_item_name", has_text=item_name)
            )
        product.locator("button").click()

    def remove_items_from_cart(self, item_names: list[str]):
        for item_name in item_names:
            self.remove_item_from_cart(item_name)

    
    



    