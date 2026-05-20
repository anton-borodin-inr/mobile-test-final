import pytest
import allure
from pages.apps_page import AppsPage

@pytest.mark.regression
@pytest.mark.apps
@allure.epic("Settings")
@allure.feature("App info window")
@allure.story("App info window can be opened")
def test_scroll_to_app_in_full_list(driver):
    apps = AppsPage(driver)
    apps.open_apps_section()
    apps.open_all_apps_list()
    apps.open_app("YouTube")
    assert apps.get_app_info_title() == "YouTube"