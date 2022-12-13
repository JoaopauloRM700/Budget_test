from appium.webdriver.common.appiumby import By
from BasePage import BasePage


class MainPage(BasePage):
    expense_option_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/btnAddExpense')
    income_option_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/btnAddIncome')


    def click_expense(self):
        expense_option = self.driver.find_element(*MainPage.expense_option_locator)
        expense_option.click()

    def click_income(self):
        income_option = self.driver.find_element(*MainPage.income_option_locator)
        income_option.click()
