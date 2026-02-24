from pages.login_page import LoginPage
from pages.hamburger_menu import HamburgerMenu
from playwright.sync_api import expect


def test_go_to_all_items(logged_in_page):
    page = logged_in_page
    menu = HamburgerMenu(page)
    menu.open_menu()
    menu.navigate_to_all_items()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_go_to_about_page(logged_in_page):
    page = logged_in_page
    menu = HamburgerMenu(page)
    menu.open_menu()
    menu.navigate_to_about()
    expect(page).to_have_url("https://saucelabs.com/")


def test_logout(logged_in_page):
    page = logged_in_page
    menu = HamburgerMenu(page)
    menu.open_menu()
    menu.logout()
    
    # Check if login btn is visible
    # Check that hamburger menu is NOT visible
    login_page = LoginPage(page)
    expect(login_page.login_button).to_be_visible()
    expect(menu.menu_button).not_to_be_visible()

    # Check direct navigation to inventory redirects to login (user cannot access)
    page.goto("https://www.saucedemo.com/inventory.html")  
    expect(login_page.get_error_message()).to_have_text("Epic sadface: You can only access '/inventory.html' when you are logged in."), "Expected error message for accessing inventory without login not displayed"




