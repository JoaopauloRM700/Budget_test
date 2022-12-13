import time

from appium.webdriver.common.appiumby import By
from MoneyTracker.PageObjects.BasePage import BasePage


class AddIncomePage(BasePage):
    date_locator_income = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvDate')
    time_locator_income = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvTime')
    account_selector_locator_income = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/spinnerAccount')
    price_locator_income = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/etPrice')
    title_locator_income = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/etTitle')
    category_locator_income = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/etCategory')
    save_button_locator_income = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/fabDone')
    select_date_locator_income = (By.XPATH, "//android.widget.TextView[contains(@text, '8')]")
    ok_date_locator_income = (By.ID, 'android:id/button1')
    select_time_locator_income = (By.XPATH, "//android.widget.TextView[contains(@text, '8')]")
    ok_time_locator_income = (By.ID, 'android:id/button1')
    account_list_locator_income = (By.ID, 'android:id/text1')

    def account_selector_click(self):
        self.driver.implicitly_wait(30)
        account_selector = self.driver.find_element(*AddIncomePage.account_selector_locator_income)
        account_selector.click()

    def account_list_select(self):
        self.driver.implicitly_wait(30)
        account_list = self.driver.find_elements(*AddIncomePage.account_list_locator_income)
        account_list[0].click()

    def type_price(self, text):
        self.driver.implicitly_wait(30)
        price = self.driver.find_element(*AddIncomePage.price_locator_income)
        price.send_keys(text)

    def type_title(self, text):
        self.driver.implicitly_wait(30)
        title = self.driver.find_element(*AddIncomePage.title_locator_income)
        title.send_keys(text)

    def type_category(self, text):
        self.driver.implicitly_wait(30)
        category = self.driver.find_element(*AddIncomePage.category_locator_income)
        category.send_keys(text)

    def date_click(self):
        self.driver.implicitly_wait(30)
        date = self.driver.find_element(*AddIncomePage.date_locator_income)
        # select_date = self.driver.find_element(*AddExpensePage.select_date_locator)
        #self.driver.hide_keyboard()
        date.click()
        ok_date = self.driver.find_element(*AddIncomePage.ok_date_locator_income)
        # select_date.click()
        ok_date.click()

    def time_click(self):
        self.driver.implicitly_wait(30)
        time = self.driver.find_element(*AddIncomePage.time_locator_income)
        time.click()
        ok_time = self.driver.find_element(*AddIncomePage.ok_time_locator_income)
        ok_time.click()

    def click_save_button_date(self):
        self.driver.implicitly_wait(30)
        save_button = self.driver.find_element(*AddIncomePage.ok_date_locator_income)
        save_button.click()

    def click_save_button_time(self):
        self.driver.implicitly_wait(30)
        save_button = self.driver.find_element(*AddIncomePage.ok_time_locator_income)
        save_button.click()

    def click_save_income(self):
        self.driver.implicitly_wait(30)
        save = self.driver.find_element(*AddIncomePage.save_button_locator_income)
        save.click()

    #def select_date_future(self):

