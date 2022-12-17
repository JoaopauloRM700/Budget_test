import time

from appium.webdriver.common.appiumby import By

from MoneyTracker.PageObjects.BasePage import BasePage


class EditDeleteIncome(BasePage):
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
    error_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/textinput_error')
    date_future = (By.XPATH, '//android.view.View[@content-desc="20 December 2022"]')
    date_past = (By.XPATH, '//android.view.View[@content-desc="12 December 2022"]')
    message_error_date = (By.XPATH, '/hierarchy/android.widget.Toast')
    delete_button_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/action_delete')

    def delete_income(self):
        delete = self.driver.find_element(*EditDeleteIncome.delete_button_locator)
        delete.click()

    def edit_price_income(self, text):
        self.driver.implicitly_wait(30)
        price = self.driver.find_element(*EditDeleteIncome.price_locator_income)
        price.send_keys(text)

    def edit_title_income(self, text):
        self.driver.implicitly_wait(30)
        title = self.driver.find_element(*EditDeleteIncome.title_locator_income)
        title.send_keys(text)

    def edit_category_income(self, text):
        self.driver.implicitly_wait(30)
        category = self.driver.find_element(*EditDeleteIncome.category_locator_income)
        category.send_keys(text)

    def click_save_income_edit(self):
        self.driver.implicitly_wait(30)
        save = self.driver.find_element(*EditDeleteIncome.save_button_locator_income)
        save.click()