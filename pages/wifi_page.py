from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class WifiPage(BasePage):
    NETWORK_INTERNET = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Network & internet")')
    INTERNET = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Internet")')
    WIFI_SWITCH = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.android.settings:id/switchWidget")')

    def open_from_home(self):
        self.click(self.NETWORK_INTERNET)
        self.click(self.INTERNET)

    def is_wifi_enabled(self):
        switch = self.find(self.WIFI_SWITCH)
        state = switch.get_attribute('checked')
        return state == 'true'

    def toggle_wifi(self):
        self.click(self.WIFI_SWITCH)