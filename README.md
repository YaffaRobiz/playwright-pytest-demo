# Playwright + pytest demo

This repository is a small demo test suite that uses Playwright (Python) together with pytest to automate the Sauce Demo web app. It includes example page objects, tests, and fixtures.

## Contents

- `pages/` - page object classes (LoginPage, InventoryPage, CartPage, HamburgerMenu, ...)
- `tests/` - pytest test cases
- `utils/` - helper utilities (data reader, test data)
- `conftest.py` - pytest fixtures that create the Playwright browser/page and provide a `logged_in_page` fixture
- `requirements.txt` - pinned Python dependencies

## Prerequisites

- Python 3.8+ installed. Verify with:

```powershell
python --version
```

- Recommended: create and use a virtual environment.

## Setup

1. Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate
```

2. Install Python dependencies:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

3. Install Playwright browsers (required once):

```powershell
python -m playwright install
```

Now you're ready to run tests.

## Running tests

- Run the full test suite:

```powershell
pytest -q
```

- Run a single test file (example):

```powershell
pytest -q tests/test_menu.py
```

- Run a single test function by name:

```powershell
pytest -q -k test_go_to_about_page
```

Notes:
- The `conftest.py` fixture in this repo launches the browser with `headless=False` and `slow_mo=200` so you can see the browser while tests run. If you want CI-friendly headless runs, change the `browser` fixture in `conftest.py` to `headless=True`.

## How the tests are organized

- Page objects live in `pages/`. Each page object encapsulates selectors and actions for a specific page (login, inventory, cart, etc.).
- Tests use pytest fixtures from `conftest.py`:
	- `page` — a fresh Playwright page for each test.
	- `logged_in_page` — a page already logged into the demo app (useful for tests that require authentication).


