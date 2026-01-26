from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.data_reader import get_json_data
import pytest

checkout_information = get_json_data("./test_data/checkout_information.json")

def test_add_items_to_cart(cart_with_items):
    cart_page, expected_items = cart_with_items
    cart_item_names = cart_page.get_cart_items_names()

    for item in expected_items:
        assert item in cart_item_names

def test_remove_items_from_cart(cart_with_items):
    cart_page, expected_items = cart_with_items
    items_to_remove = expected_items[:2]

    cart_page.remove_items_from_cart(items_to_remove)
    cart_item_names = cart_page.get_cart_items_names()

    for item in items_to_remove:
        assert item not in cart_item_names
    
def test_checkout_success(cart_with_items):
    cart_page, _ = cart_with_items
    cart_page.click_checkout_button()
    checkout_page = CheckoutPage(cart_page.page)
    checkout_input = checkout_information
    checkout_page.fill_checkout_information(
        checkout_input["first_name"],
        checkout_input["last_name"],
        checkout_input["postal_code"]
    )

    checkout_page.continue_button.click()
    checkout_page.finish_button.click()
    assert cart_page.page.get_by_text("THANK YOU FOR YOUR ORDER").is_visible()