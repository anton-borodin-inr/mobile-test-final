from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class AboutPage(BasePage):
    ABOUT_PHONE = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().resourceId("com.android.settings:id/recycler_view"))'
        '.scrollIntoView(new UiSelector().text("About emulated device"))'
    )

    def open_from_home(self):
        self.click(self.ABOUT_PHONE)

    def get_field_value(self, field_name):
        #Выполняется скролл до искомого элемента с задаваемым title
        scroll_locator = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true))'
            f'.scrollIntoView(new UiSelector().text("{field_name}"))'
        )
        self.find(scroll_locator)

        #Читаем значение рядом с этим title
        value_locator = (
            AppiumBy.XPATH,
            f'//android.widget.TextView[@resource-id="android:id/title" and @text="{field_name}"]'
            f'/following-sibling::android.widget.TextView[@resource-id="android:id/summary"]'
        )

        return self.get_text(value_locator)