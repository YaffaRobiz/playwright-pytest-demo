from pages.login_page import LoginPage
from utils.data_reader import get_json_data
import pytest
from playwright.sync_api import expect

credentials = get_json_data("./test_data/login_test_data.json")

@pytest.mark.parametrize("data", credentials)
def test_valid_login(page, data):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(data["username"], data["password"])
    # Verify successful login by checking URL
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


def test_locked_out_user(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")
    expect(login_page.get_error_message()).to_have_text("Epic sadface: Sorry, this user has been locked out."), "Expected error message for locked out user not displayed"

def test_empty_username_and_password(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("", "")
    expect(login_page.get_error_message()).to_have_text("Epic sadface: Username is required"),"Expected error message for empty username and password not displayed"

def test_empty_password(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "")
    expect(login_page.get_error_message()).to_have_text("Epic sadface: Password is required"),"Expected error message for empty password not displayed"

def test_empty_username(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("", "secret_sauce")
    expect(login_page.get_error_message()).to_have_text("Epic sadface: Username is required"), "Expected error message for empty username not displayed"

def test_invalid_username_and_password(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("invalid_user", "invalid_password")
    expect(login_page.get_error_message()).to_have_text("Epic sadface: Username and password do not match any user in this service"), "Expected error message for invalid username and password not displayed"


