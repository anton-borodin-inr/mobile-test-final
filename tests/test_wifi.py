import pytest
import allure
from pages.wifi_page import WifiPage

@pytest.mark.smoke
@pytest.mark.wifi
@allure.epic("Settings")
@allure.feature("Wi-Fi")
@allure.story("Toggle Wi-Fi changes state")
@allure.title("Wi-Fi toggle changes its state")
@allure.severity(allure.severity_level.CRITICAL)
def test_wifi_toggle_changes_state(driver):
    wifi_page = WifiPage(driver)
    wifi_page.open_from_home() #open Wi-Fi page
    initial_state = wifi_page.is_wifi_enabled()
    wifi_page.toggle_wifi() #toggle Wi-Fi switch
    new_state = wifi_page.is_wifi_enabled()
    assert new_state != initial_state, f"Wi-Fi state did not change. Was: {initial_state}, now {new_state}"