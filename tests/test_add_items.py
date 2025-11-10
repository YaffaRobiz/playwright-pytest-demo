import pytest
from playwright.sync_api import sync_playwright
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_products_displayed(logged_in_page):
    page = logged_in_page
    inventory_page = InventoryPage(page)
    product_titles = inventory_page.get_product_titles()
    assert len(product_titles) > 0, "No products found on the inventory page."
    print(f"Test passed: {len(product_titles)} products found on the inventory page.")

def test_add_item_to_cart(logged_in_page):
    page = logged_in_page
    inventory_page = InventoryPage(page)
    product_titles = inventory_page.get_product_titles()
    first_product = product_titles[0]

    # Add first product to cart
    inventory_page.add_to_cart_buttons.nth(0).click()
    # Go to cart
    inventory_page.go_to_cart()
    # Verify item is in cart
    cart_page = CartPage(page)
    cart_items = cart_page.get_cart_items()
    print(type(cart_items))
    assert first_product in cart_items, f"{first_product} not found in cart." 
    print(f"Test passed: {first_product} successfully added to cart.") 
    

