# Android Settings UI Automation
Automated UI tests for Android Settings app using Appium + pytest. Demonstrates Page Object Model, data-driven testing, and Allure reporting.

> Final project for QA Automation course

## Tech stack

- Language & Test Framework: Python 3.14, pytest, Allure
- Mobile Automation: Appium-Python-Client 5.3.1, Appium Server 3.3.1, uiautomator2 driver
- Target Platform: Android 15 (Pixel 7 emulator)

## Test coverage

- About phone - 4 parametrized checks of fields (data-driven from JSON) 
- Apps - scroll to element in Compose UI (swipe-loop)
- Display - brightness slider, move from 100% to 0% (W3C Actions)
- Search - search for an exact setting and check that the result appears
- Wi-Fi - toggle Wi-Fi switch on/off

## Project structure
```
├── pages/          - Page Object classes (one per screen)
│   ├── about_page.py
│   ├── apps_page.py
│   ├── base_page.py
│   ├── display_page.py
│   ├── search_page.py
│   └── wifi_page.py    
├── test_data/      - test data in JSON format
│   └── about_phone.json      - information about phone
├── tests/          - files with tests
│   ├── test_about.py
│   ├── test_apps.py
│   ├── test_display.py
│   ├── test_search.py
│   └── test_wifi.py
├── conftest.py      - file with fixtures
├── pytest.ini       - pytest configuration (markers, addopts)
├── requirements.txt       - Python dependencies
└── README.md
```

## Prerequisites
- Android Studio with Pixel 7 (emulator, Android 15) created and running
- `adb devices` shows the emulator
- Appium Server should be launched on http://localhost:4723
- JDK 11+ installed
- Appium uiautomator2 driver (installed in Setup step below)

## Setup
```bash
git clone https://github.com/anton-borodin-inr/mobile-test-final
cd mobile-test-final
appium driver install uiautomator2
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## How to run tests
1. Start the Android emulator
2. Launch Appium Server:
```bash
appium
```
3. Run tests:
```bash
# run all tests
pytest -v

# only smoke tests
pytest -m smoke

# run tests with Allure report
pytest --alluredir=allure-results
allure serve allure-results
```

## Architecture Highlights
- Page Object Model - each screen is a class inheriting from BasePage
- Driver fixture with `terminate_app + activate_app` for test isolation
- Compose UI workaround: manual swipe-loop instead of UiScrollable (UiScrollable doesn't reliably work on Compose UI, so manual swipe + sleep is used to wait for inertial scroll to settle)