from pages.login_page import LoginPage
from utils.data_reader import get_json_data
import pytest

test_data = get_json_data("./test_data/login_test_data.json")

@pytest.mark.parametrize("data", test_data)
def test_valid_login(page, data):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(data["username"], data["password"])
    # Verify successful login by checking URL
    assert page.url == "https://www.saucedemo.com/inventory.html"

def test_locked_out_user(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")
    assert login_page.get_error_message() == "Epic sadface: Sorry, this user has been locked out."

def test_empty_username_and_password(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("", "")
    assert login_page.get_error_message() == "Epic sadface: Username is required"

def test_empty_password(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "")
    assert login_page.get_error_message() == "Epic sadface: Password is required" 

def test_empty_username(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("", "secret_sauce")
    assert login_page.get_error_message() == "Epic sadface: Username is required"

def test_invalid_username_and_password(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("invalid_user", "invalid_password")
    assert login_page.get_error_message() == "Epic sadface: Username and password do not match any user in this service"


