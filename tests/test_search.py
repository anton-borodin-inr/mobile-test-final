import pytest
import allure
from pages.search_page import SearchPage

@allure.epic("Settings")
@allure.feature("Search")
@pytest.mark.smoke
@pytest.mark.search
@allure.story("Search returns relevant results")
def test_search_finds_bluetooth(driver):
    search_page = SearchPage(driver)

    with allure.step("Open search"):
        search_page.open_search()

    with allure.step("Enter search query 'Bluetooth'"):
        search_page.enter_search_query('Bluetooth')

    with allure.step("Get search result"):
        results = search_page.ger_search_results()

    with allure.step("Verify at least one result contains 'Bluetooth'"):
        matching = [r for r in results if "bluetooth" in r.lower()]
        assert len(matching) > 0, (
            f"No results contain 'Bluetooth'. Got: {results}"
        )