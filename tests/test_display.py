import time
import pytest
import allure
from pages.display_page import DisplayPage

@allure.epic("Settings")
@allure.feature("Display")
@pytest.mark.smoke
@pytest.mark.display
@allure.story("Brightness slider can be moved")
def test_brightness_slider_value(driver):
    display_page = DisplayPage(driver)

    with allure.step("Open Display screen"):
        display_page.open_from_home()

    with allure.step("Read initial brightness value"):
        initial_value = display_page.get_brightness_value()

    with allure.step("Open brightness slider"):
        display_page.click_on_brightness_button()

    with allure.step("Drag brightness slider to the left"):
        display_page.drag_slider_to_left_edge()
        time.sleep(1)

    with allure.step("Close slider overlay"):
        display_page.close_slider()
        time.sleep(1)

    with allure.step("Verify brightness value has changed"):
        new_value = display_page.get_brightness_value()
        assert new_value != initial_value, (
            f"Brightness value did not change. Was: {initial_value}, now: {new_value}"
        )