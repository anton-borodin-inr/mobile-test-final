import pytest
import allure
from pages.wifi_page import WifiPage

@allure.epic("Settings")
@allure.feature("Wi-Fi")
@pytest.mark.smoke
@pytest.mark.wifi
@allure.story("Toggle Wi-Fi changes state")
def test_wifi_toggle_changes_state(driver):
    wifi_page = WifiPage(driver)

    with allure.step("Open Wi-Fi screen"):
        wifi_page.open_from_home()

    with allure.step("Read initial Wi-Fi state"):
        initial_state = wifi_page.is_wifi_enabled()

    with allure.step("Toggle Wi-Fi"):
        wifi_page.toggle_wifi()

    with allure.step("Verify Wi-Fi state has changed"):
        new_state = wifi_page.is_wifi_enabled()
        assert new_state != initial_state, f"Wi-Fi state did not change. Was: {initial_state}, now {new_state}"