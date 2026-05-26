import pytest
import allure
from pages.search_page import SearchPage

@pytest.mark.smoke
@pytest.mark.search
@allure.epic("Settings")
@allure.feature("Search")
@allure.story("Search returns relevant results")
@allure.title("Search returns lines with 'Bluetooth' as result")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_finds_bluetooth(driver):
    search_page = SearchPage(driver)
    search_page.open_search() #tap on search bar
    search_page.enter_search_query('Bluetooth') #enter "Bluetooth"
    results = search_page.get_search_results() #get search results
    matching = [r for r in results if "bluetooth" in r.lower()] #Verify at least one result contains "Bluetooth"
    assert len(matching) > 0, (
        f"No results contain 'Bluetooth'. Got: {results}"
    )