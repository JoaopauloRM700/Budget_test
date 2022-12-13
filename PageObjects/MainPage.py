from appium.webdriver.common.appiumby import AppiumBy
from BasePage import BasePage

class MainPage(BasePage):

    MoneyTracker_option_locator = (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]')

    def click_budget(self):
        MoneyTracker_option = self.driver.find_element(*MainPage.MoneyTracker_option_locator)
        MoneyTracker_option.click()

