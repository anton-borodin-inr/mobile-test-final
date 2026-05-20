from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException

class AppsPage(BasePage):
    APPS_ENTRY = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Apps")')
    SEE_ALL_APPS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("See all")')
    APP_INFO_TITLE = (
    AppiumBy.XPATH,
    '(//android.widget.ScrollView//android.widget.TextView)[1]'
    )

    def open_apps_section(self):
        self.click(self.APPS_ENTRY)

    def open_all_apps_list(self):
        self.click(self.SEE_ALL_APPS)

    def scroll_to_app(self, app_name: str, max_swipes: int = 15):
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{app_name}")')

        for _ in range(max_swipes):
            elements = self.driver.find_elements(*locator)
            if elements:
                return elements[0]
            # свайп для перемещения по ссписку вниз
            self.swipe_by_coordinates(540, 1800, 540, 800)

        raise NoSuchElementException(f"App {app_name} not found after {max_swipes} swipes")


    def open_app(self, app_name: str):
        self.scroll_to_app(app_name).click()

    def get_app_info_title(self) -> str:
        return self.get_text(self.APP_INFO_TITLE)