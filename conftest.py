import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage  


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=200)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    # Create a new page for each test.
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()



@pytest.fixture(scope="session")
def logged_in_page(browser):
        context = browser.new_context()
        page = context.new_page()

        # ---- LOGIN STEPS ----
        login_page = LoginPage(page)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")    

        # wait for login confirmation (e.g., inventory page loaded)
        page.wait_for_url("**/inventory.html")

        yield page  # <-- hand over the logged-in page to the test

        # ---- CLEANUP ----
        context.close()
