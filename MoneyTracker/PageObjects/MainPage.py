from appium.webdriver.common.appiumby import By, AppiumBy
from BasePage import BasePage


class MainPage(BasePage):
    expense_option_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/btnAddExpense')
    income_option_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/btnAddIncome')
    new_title_element_locator = (By.XPATH,
                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView[1]')
    new_price_element_locator = (By.XPATH,
                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView[1]')
    new_element_locator = (By.XPATH,
                           '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[3]/android.widget.LinearLayout')

    def click_expense(self):
        expense_option = self.driver.find_element(*MainPage.expense_option_locator)
        expense_option.click()

    def click_income(self):
        income_option = self.driver.find_element(*MainPage.income_option_locator)
        income_option.click()

    def new_title_element_add_income(self):
        new_element_add = self.driver.find_element(*MainPage.new_title_element_locator)
        return new_element_add.text

    def new_price_element_add_income(self):
        new_element_add = self.driver.find_element(*MainPage.new_price_element_locator)
        return new_element_add.text

    def click_new_element(self):
        new_element = self.driver.find_element(*MainPage.new_element_locator)
        new_element.click()
