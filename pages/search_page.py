from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class SearchPage(BasePage):
    SEARCH_ICON = (AppiumBy.ID, "com.android.settings:id/search_action_bar")
    SEARCH_INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    SEARCH_RESULT = (AppiumBy.ID, "android:id/title")

    def open_search(self):
        self.click(self.SEARCH_ICON)

    def enter_search_query(self, query):
        input_field = self.find(self.SEARCH_INPUT)
        input_field.clear()
        input_field.send_keys(query)

    def ger_search_results(self):
        elements = self.find_all(self.SEARCH_RESULT)
        return [el.text for el in elements]