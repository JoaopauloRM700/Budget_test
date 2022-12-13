import unittest
import warnings

import self as self
from datetime import date
from MoneyTracker.PageObjects.MainPage import MainPage
from MoneyTracker.PageObjects.AddIncomePage import AddIncomePage
from MoneyTracker.PageObjects.Data import TestData
from MoneyTracker.PageObjects.AddExpensePage import AddExpensePage
from appium import webdriver


class MyTestCase(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'emulator-5556'
        desired_caps['appPackage'] = 'com.blogspot.e_kanivets.moneytracker'
        desired_caps['appActivity'] = '.activity.record.MainActivity'
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def test_add_new_income(self):
        main_page = MainPage(self.driver)
        main_page.click_income()
        self.driver.implicitly_wait(30)
        add_income_page = AddIncomePage(self.driver)
        add_income_page.type_price(TestData.Price)
        add_income_page.type_title(TestData.Title)
        add_income_page.type_category(TestData.Category)
        add_income_page.time_click()
        add_income_page.date_click()
        add_income_page.account_list_select()
        add_income_page.click_save_income()



if __name__ == '__main__':
    unittest.main()
