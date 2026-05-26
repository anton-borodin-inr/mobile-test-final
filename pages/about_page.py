import allure
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class AboutPage(BasePage):
    ABOUT_PHONE = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().resourceId("com.android.settings:id/recycler_view"))'
        '.scrollIntoView(new UiSelector().text("About emulated device"))'
    )

    @allure.step("Open 'About emulated device' page")
    def open_from_home(self):
        self.click(self.ABOUT_PHONE)

    @allure.step("Scroll to {field_name}")
    def get_field_value(self, field_name):
        #Scroll to exact element with title
        scroll_locator = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true))'
            f'.scrollIntoView(new UiSelector().text("{field_name}"))'
        )
        self.find(scroll_locator)

        #Read value near title
        value_locator = (
            AppiumBy.XPATH,
            f'//android.widget.TextView[@resource-id="android:id/title" and @text="{field_name}"]'
            f'/following-sibling::android.widget.TextView[@resource-id="android:id/summary"]'
        )

        return self.get_text(value_locator)