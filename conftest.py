import allure
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.platform_version = "15"
    options.device_name = "emulator-5554"
    options.app_package = "com.android.settings"
    options.app_activity = ".Settings"
    options.automation_name = "UiAutomator2"
    options.no_reset = True

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    #Запуск со свежего Settings на главном экране
    driver.terminate_app("com.android.settings")
    driver.activate_app("com.android.settings")

    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshot = driver.get_screenshot_as_png()
            allure.attach(
                body=screenshot,
                name=f"screenshot_{item.name}",
                attachment_type=allure.attachment_type.PNG
            )