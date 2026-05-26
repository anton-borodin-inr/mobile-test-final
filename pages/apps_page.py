import time
import allure
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException

class AppsPage(BasePage):
    APPS_ENTRY = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Apps")')
    SEE_ALL_APPS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("All apps")')
    APP_INFO_TITLE = (
    AppiumBy.XPATH,
    '(//android.widget.ScrollView//android.widget.TextView)[1]'
    )

    @allure.step("Open 'Apps' page")
    def open_apps_section(self):
        self.click(self.APPS_ENTRY)

    @allure.step("Open 'All apps' page")
    def open_all_apps_list(self):
        self.click(self.SEE_ALL_APPS)

    @allure.step("Scroll to app {app_name}")
    def scroll_to_app(self, app_name: str, max_swipes: int = 15):
        locator = (
            AppiumBy.XPATH,
            f'//android.view.View[@clickable="true"][.//android.widget.TextView[@text="{app_name}"]]'
        )

        for _ in range(max_swipes):
            elements = self.driver.find_elements(*locator)
            if elements:
                time.sleep(0.5)
                return elements[0]
            # свайп для перемещения по ссписку вниз
            self.swipe_by_coordinates(540, 1800, 540, 800)

        raise NoSuchElementException(f"App {app_name} not found after {max_swipes} swipes")


    @allure.step("Open {app_name} page")
    def open_app(self, app_name: str):
        self.scroll_to_app(app_name).click()

    @allure.step("Check if 'App info' page exists")
    def get_app_info_title(self) -> str:
        return self.get_text(self.APP_INFO_TITLE)