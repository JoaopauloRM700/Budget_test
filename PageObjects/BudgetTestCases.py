import unittest
import warnings
from datetime import date

from MainPage import MainPage
from BudgetPage import BudgetPage
from AddBudgetPage import AddBudgetPage
from appium import webdriver
from Data import TestData
import time

from PageObjects.IntroPage import IntroPage


class MyTestCase(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'emulator-5556'
        desired_caps['appPackage'] = 'protect.budgetwatch'
        desired_caps['appActivity'] = '.MainActivity'
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def test_app_budget_add(self):
        intro_page = IntroPage(self.driver)
        intro_page.click_skip()
        self.driver.implicitly_wait(30)
        main_page = MainPage(self.driver)
        main_page.click_budget()
        budget_page = BudgetPage(self.driver)
        budget_page.click_add()
        add_page = AddBudgetPage(self.driver)
        self.driver.implicitly_wait(30)
        add_page.type_budget_type(TestData.budget_type)
        add_page.type_budget_value(TestData.budget_value)
        add_page.click_save_button()
        budget_page = BudgetPage(self.driver)
        self.assertEqual(budget_page.get_first_budget(), TestData.budget_type)

    def test_app_budget_add_nome_invalid(self):
        self.driver.implicitly_wait(30)
        intro_page = IntroPage(self.driver)
        intro_page.click_skip()
        # clicar em budget
        main_page = MainPage(self.driver)
        main_page.click_budget()
        budget_page = BudgetPage(self.driver)
        budget_page.click_add()
        add_page = AddBudgetPage(self.driver)
        self.driver.implicitly_wait(20)
        time.sleep(5)
        add_page.type_budget_value(TestData.budget_value)
        add_page.click_save_button()
        self.assertEqual(add_page.get_error(), TestData.msg_budget_type_empty)

    def test_app_budget_add_value_invalid(self):
        self.driver.implicitly_wait(30)
        intro_page = IntroPage(self.driver)
        intro_page.click_skip()
        # clicar em budget
        main_page = MainPage(self.driver)
        main_page.click_budget()
        budget_page = BudgetPage(self.driver)
        budget_page.click_add()
        # Adicionar nome
        add_page = AddBudgetPage(self.driver)
        self.driver.implicitly_wait(30)
        add_page.type_budget_type(TestData.budget_type)
        # Adicionar valor
        self.driver.implicitly_wait(20)
        time.sleep(5)
        add_page.type_budget_value(TestData.budget_value_invalid)
        # Save
        add_page.click_save_button()
        # Validação
        self.assertEqual(add_page.get_error(), TestData.msg_budget_value_empty)

    def test_app_budget_add_nome_acima_30(self):
        intro_page = IntroPage(self.driver)
        intro_page.click_skip()
        self.driver.implicitly_wait(30)
        main_page = MainPage(self.driver)
        main_page.click_budget()
        budget_page = BudgetPage(self.driver)
        budget_page.click_add()
        add_page = AddBudgetPage(self.driver)
        self.driver.implicitly_wait(30)
        add_page.type_budget_type(TestData.budget_type_invalid)
        add_page.type_budget_value(TestData.budget_value)
        add_page.click_save_button()
        self.assertEqual(add_page.get_error(), TestData.msg_budget_type_empty)

    def test_app_budget_add_valor_10(self):
        intro_page = IntroPage(self.driver)
        intro_page.click_skip()
        self.driver.implicitly_wait(30)
        main_page = MainPage(self.driver)
        main_page.click_budget()
        budget_page = BudgetPage(self.driver)
        budget_page.click_add()
        add_page = AddBudgetPage(self.driver)
        self.driver.implicitly_wait(30)
        add_page.type_budget_type(TestData.budget_type)
        add_page.type_budget_value(TestData.budget_value_10char_invalid)
        add_page.click_save_button()
        self.assertEqual(add_page.get_error(), TestData.msg_budget_value_empty)

    def test_app_budget_add_valor_acima_10(self):
        intro_page = IntroPage(self.driver)
        intro_page.click_skip()
        self.driver.implicitly_wait(30)
        main_page = MainPage(self.driver)
        main_page.click_budget()
        budget_page = BudgetPage(self.driver)
        budget_page.click_add()
        add_page = AddBudgetPage(self.driver)
        self.driver.implicitly_wait(30)
        add_page.type_budget_type(TestData.budget_type)
        add_page.type_budget_value(TestData.budget_value_10char_invalid)
        add_page.click_save_button()
        self.assertEqual(add_page.get_error(), TestData.msg_budget_value_empty)

if __name__ == '__main__':
    unittest.main()
