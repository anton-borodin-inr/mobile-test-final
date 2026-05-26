import allure
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class DisplayPage(BasePage):
    DISPLAY = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true))'
        '.scrollIntoView(new UiSelector().text("Display & touch"))'
    )
    BRIGHTNESS_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Brightness level")')
    BRIGHTNESS_SLIDER = (AppiumBy.ID, "com.android.systemui:id/slider")
    BRIGHTNESS_VALUE = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("android:id/summary").textContains("%")'
    )

    @allure.step("Open Display screen")
    def open_from_home(self):
        self.click(self.DISPLAY)

    @allure.step("Read initial brightness value")
    def get_brightness_value(self):
        return self.get_text(self.BRIGHTNESS_VALUE)

    @allure.step("Open brightness slider")
    def click_on_brightness_button(self):
        self.click(self.BRIGHTNESS_BUTTON)

    @allure.step("Tap on the middle of the slider and drag to the left")
    def drag_slider_to_left_edge(self):
        slider = self.find(self.BRIGHTNESS_SLIDER)
        location = slider.location
        size = slider.size
        start_x = location["x"] + size["width"] // 2
        end_x = location["x"]
        start_y = end_y = location["y"] + size["height"] // 2
        self.swipe_by_coordinates(start_x, start_y, end_x, end_y)

    @allure.step("Close slider overlay")
    def close_slider(self):
        self.driver.back()



