import time
import pytest
import allure
from pages.display_page import DisplayPage

@pytest.mark.smoke
@pytest.mark.display
@allure.epic("Settings")
@allure.feature("Display")
@allure.story("Brightness slider can be moved")
@allure.title("Brightness slider can be moved from 100% to 0%")
@allure.severity(allure.severity_level.CRITICAL)
def test_brightness_slider_value(driver):
    display_page = DisplayPage(driver)
    display_page.open_from_home() #open "Display" screen
    initial_value = display_page.get_brightness_value() #get brightness value
    display_page.click_on_brightness_button() #open slider
    display_page.drag_slider_to_left_edge() #drag slider
    time.sleep(1) #wait 1 second
    display_page.close_slider() #use "back" button
    time.sleep(1) #wait 1 second
    new_value = display_page.get_brightness_value() #Verify brightness value has changed
    assert new_value != initial_value, (
        f"Brightness value did not change. Was: {initial_value}, now: {new_value}"
    )