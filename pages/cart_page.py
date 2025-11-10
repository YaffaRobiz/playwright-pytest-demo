
class CartPage:
    def __init__(self, page):
        self.page = page
        # self.cart_items_selector = ".cart_item"
        self.cart_items = page.locator(".cart_item .inventory_item_name").all_inner_texts()
        self.continue_shopping_button = page.locator("[data-test=\"continue-shopping\"]")
        self.checkout_button = page.locator("[data-test=\"checkout\"]")
        self.remove_item_button = page.locator("[data-test^=\"remove-\"]")

    def get_cart_items(self):
        return self.cart_items
    
    def continue_shopping(self):
        self.continue_shopping_button.click()

    def remove_item(self, item_name):
        count = self.cart_items.count()
        for i in range(count):
            name = self.cart_items.nth(i).inner_text()
            if name == item_name:
                self.remove_item_button.nth(i).click()
            else:
                print(f"Item '{item_name}' not found in cart.")
                

    def proceed_to_checkout(self):
        self.checkout_button.click()

    