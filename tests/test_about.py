import json
import pytest
import allure
from pages.about_page import AboutPage

def load_expected_fields():
    with open("test_data/about_phone.json", encoding="utf-8") as f:
        return list(json.load(f).items())

@pytest.mark.regression
@pytest.mark.parametrize("field_name, expected_value", load_expected_fields())
@allure.epic("Settings")
@allure.feature("About phone")
@allure.story("Phone info displays correct values")
@allure.title("About phone: {field_name} = {expected_value}")
@allure.severity(allure.severity_level.NORMAL)
def test_about_phone_field_value(driver, field_name, expected_value):
    about_page = AboutPage(driver)
    about_page.open_from_home() #Open About phone screen
    actual_value = about_page.get_field_value(field_name)
    assert actual_value == expected_value, (
        f"Field '{field_name}': '{expected_value}', got '{actual_value}'"
    )