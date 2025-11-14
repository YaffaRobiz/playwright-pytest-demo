from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_products_displayed(logged_in_page):
    page = logged_in_page
    inventory_page = InventoryPage(page)
    product_titles = inventory_page.count_items()
    assert product_titles > 0, "No products found on the inventory page."
    

# def test_add_items_to_cart(logged_in_page):
