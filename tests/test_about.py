import json
import pytest
import allure
from pages.about_page import AboutPage

def load_expected_fields():
    with open("test_data/about_phone.json", encoding="utf-8") as f:
        return list(json.load(f).items())

@allure.epic("Settings")
@allure.feature("About phone")
@pytest.mark.regression
@pytest.mark.parametrize("field_name, expected_value", load_expected_fields())
def test_about_phone_field_value(driver, field_name, expected_value):
    allure.dynamic.story(f"Verify {field_name}")

    about_page = AboutPage(driver)

    with allure.step("Open About phone screen"):
        about_page.open_from_home()

    with allure.step(f"Read value of '{field_name}'"):
        actual_value = about_page.get_field_value(field_name)

    with allure.step(f"Verify '{field_name}' is equal to '{expected_value}'"):
        assert actual_value == expected_value, (
            f"Field '{field_name}': '{expected_value}', got '{actual_value}'"
        )