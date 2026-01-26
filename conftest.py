import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=200)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture
def logged_in_page(browser):
        context = browser.new_context()
        page = context.new_page()

        # ---- LOGIN STEPS ----
        login_page = LoginPage(page)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")    

        page.wait_for_url("**/inventory.html")

        yield page

        context.close()


@pytest.fixture
def cart_with_items(logged_in_page):
    page = logged_in_page
    inventory_page = InventoryPage(page)
    items = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Fleece Jacket"
        ]
    
    inventory_page.add_items_to_cart(items)
    inventory_page.go_to_cart()
    
    return CartPage(page), items