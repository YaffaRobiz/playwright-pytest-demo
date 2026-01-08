from pages.login_page import LoginPage
from pages.hamburger_menu import HamburgerMenu
from playwright.sync_api import expect
import pytest



def test_go_to_all_items(logged_in_page):
    page = logged_in_page
    menu = HamburgerMenu(page)
    menu.open_menu()
    menu.navigate_to_all_items()
    assert page.url == "https://www.saucedemo.com/inventory.html"

def test_go_to_about_page(logged_in_page):
    page = logged_in_page
    menu = HamburgerMenu(page)
    menu.open_menu()
    menu.navigate_to_about()
    assert page.url == "https://saucelabs.com/"


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
    assert login_page.get_error_message() == "Epic sadface: You can only access '/inventory.html' when you are logged in."




