from appium.webdriver.common.appiumby import By
from MoneyTracker.PageObjects.BasePage import BasePage


class AddExpensePage(BasePage):
    date_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvDate')
    time_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvTime')
    account_selector_locator = (By.ID, 'android:id/text1t')

    price_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/etPrice')
    title_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/etTitle')
    category_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/etCategory')
    save_button_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/fabDone')
    select_date_locator = (By.XPATH, "//android.widget.TextView[contains(@text, '8')]")
    ok_date_locator = (By.ID, 'android:id/button1')
    select_time_locator = (By.XPATH, "//android.widget.TextView[contains(@text, '8')]")
    ok_time_locator = (By.ID, 'android:id/button1')
    account_list_locator = (By.ID, 'android:id/text1')

    def account_selector_click(self):
        account_selector = self.driver.find_element(*AddExpensePage.account_selector_locator)
        account_selector.click()

    def account_list_select(self):
        account_list = self.driver.find_elements(*AddExpensePage.account_list_locator)
        account_list[0].click()

    def type_price(self, text):
        price = self.driver.find_element(*AddExpensePage.price_locator)
        price.send_keys(text)

    def type_title(self, text):
        title = self.driver.find_element(*AddExpensePage.title_locator)
        title.send_keys(text)

    def type_category(self, text):
        category = self.driver.find_element(*AddExpensePage.category_locator)
        category.send_keys(text)

    def date_click(self):

        date = self.driver.find_element(*AddExpensePage.date_locator)
        # select_date = self.driver.find_element(*AddExpensePage.select_date_locator)
        date.click()
        self.driver.implicitly_wait(30)
        ok_date = self.driver.find_element(*AddExpensePage.ok_date_locator)
        # select_date.click()
        ok_date.click()

    def time_click(self):
        time = self.driver.find_element(*AddExpensePage.time_locator)
        time.click()
        self.driver.implicitly_wait(30)
        ok_time = self.driver.find_element(*AddExpensePage.ok_time_locator)
        ok_time.click()

    def click_save_button(self):
        save_button = self.driver.find_element(*AddExpensePage.save_button_locator)
        save_button.click()