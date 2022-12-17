import unittest
import warnings

import self as self
from datetime import date

from selenium.webdriver.common.by import By

from MoneyTracker.PageObjects.EditDeleteIncome import EditDeleteIncome
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
        add_income_page.account_selector_click()
        self.driver.implicitly_wait(40)
        add_income_page.account_list_select()
        add_income_page.click_save_income()
        main_page = MainPage(self.driver)
        self.assertEqual(main_page.new_title_element_add_income(), TestData.Title)

    # - Campo price possui limite de 13 caracteres, só aceita números e não pode ser vazio

    def test_price_13_caracter(self):
        main_page = MainPage(self.driver)
        main_page.click_income()
        self.driver.implicitly_wait(30)
        add_income_page = AddIncomePage(self.driver)
        add_income_page.time_click()
        add_income_page.date_click()
        add_income_page.account_selector_click()
        self.driver.implicitly_wait(30)
        add_income_page.account_list_select()
        add_income_page.type_title(TestData.Title)
        add_income_page.type_category(TestData.Category)
        add_income_page.type_price(TestData.Price_13)
        add_income_page.click_save_income()
        main_page = MainPage(self.driver)
        self.assertEqual(main_page.new_price_element_add_income(), "+ " + TestData.Price_13)

    def test_price_14_caracter(self):
        main_page = MainPage(self.driver)
        main_page.click_income()
        self.driver.implicitly_wait(30)
        add_income_page = AddIncomePage(self.driver)
        add_income_page.time_click()
        add_income_page.date_click()
        add_income_page.account_selector_click()
        self.driver.implicitly_wait(30)
        add_income_page.account_list_select()
        add_income_page.type_title(TestData.Title)
        add_income_page.type_category(TestData.Category)
        add_income_page.type_price(TestData.Price_14)
        add_income_page.click_save_income()
        self.assertEqual(add_income_page.get_error_income(), TestData.Error_limit)

    def test_price_vazio(self):
        main_page = MainPage(self.driver)
        main_page.click_income()
        self.driver.implicitly_wait(30)
        add_income_page = AddIncomePage(self.driver)
        add_income_page.time_click()
        add_income_page.date_click()
        add_income_page.account_selector_click()
        self.driver.implicitly_wait(40)
        add_income_page.account_list_select()
        add_income_page.type_title(TestData.Title)
        add_income_page.type_category(TestData.Category)
        add_income_page.click_save_income()
        self.assertEqual(add_income_page.get_error_income(), TestData.Error_field_empty)

    # Campo Category não pode ser vazio e so deve aceitar letras

    def test_category_vazio(self):
        main_page = MainPage(self.driver)
        main_page.click_income()
        self.driver.implicitly_wait(30)
        add_income_page = AddIncomePage(self.driver)
        add_income_page.time_click()
        add_income_page.date_click()
        add_income_page.account_selector_click()
        self.driver.implicitly_wait(40)
        add_income_page.account_list_select()
        add_income_page.type_title(TestData.Title)
        add_income_page.type_price(TestData.Price)
        add_income_page.click_save_income()
        self.assertEqual(add_income_page.get_error_income(), TestData.Error_field_empty)

    def test_category_com_num(self):
        main_page = MainPage(self.driver)
        main_page.click_income()
        self.driver.implicitly_wait(30)
        add_income_page = AddIncomePage(self.driver)
        add_income_page.time_click()
        add_income_page.date_click()
        add_income_page.account_selector_click()
        self.driver.implicitly_wait(40)
        add_income_page.account_list_select()
        add_income_page.type_title(TestData.Title)
        add_income_page.type_price(TestData.Price)
        add_income_page.type_category(TestData.Category_num)
        add_income_page.click_save_income()
        self.assertEqual(add_income_page.get_error_income(), TestData.Error_field_empty)


    # Pode salvar income/expense de datas no passado e no presente somente

    def test_date_past(self):
        main_page = MainPage(self.driver)
        main_page.click_income()
        self.driver.implicitly_wait(30)
        add_income_page = AddIncomePage(self.driver)
        add_income_page.type_price(TestData.Price)
        add_income_page.type_title(TestData.Title)
        add_income_page.type_category(TestData.Category)
        add_income_page.time_click()
        add_income_page.past_date()
        add_income_page.account_selector_click()
        self.driver.implicitly_wait(40)
        add_income_page.account_list_select()
        add_income_page.click_save_income()
        main_page = MainPage(self.driver)
        self.assertEqual(main_page.new_title_element_add_income(), TestData.Title)

    def test_date_future(self):
        main_page = MainPage(self.driver)
        main_page.click_income()
        self.driver.implicitly_wait(30)
        add_income_page = AddIncomePage(self.driver)
        add_income_page.type_price(TestData.Price)
        add_income_page.type_title(TestData.Title)
        add_income_page.type_category(TestData.Category)
        add_income_page.time_click()
        add_income_page.account_selector_click()
        self.driver.implicitly_wait(40)
        add_income_page.account_list_select()
        add_income_page.future_date()
        self.assertEqual(add_income_page.get_error_future_date(), TestData.Error_date_future)

    def test_edit_income(self):
        main_page = MainPage(self.driver)
        main_page.click_income()
        self.driver.implicitly_wait(30)
        add_income_page = AddIncomePage(self.driver)
        add_income_page.type_price(TestData.Price)
        add_income_page.type_title(TestData.Title)
        add_income_page.type_category(TestData.Category)
        add_income_page.time_click()
        add_income_page.date_click()
        add_income_page.account_selector_click()
        self.driver.implicitly_wait(40)
        add_income_page.account_list_select()
        add_income_page.click_save_income()
        main_page = MainPage(self.driver)
        main_page.click_new_element()
        deleteEdit_page = EditDeleteIncome(self.driver)
        #deleteEdit_page.edit_category_income(TestData.Category_edit)
        #deleteEdit_page.edit_price_income(TestData.Price_edit)
        deleteEdit_page.edit_title_income(TestData.Title_edit)
        deleteEdit_page.click_save_income_edit()
        self.assertEqual(main_page.new_title_element_add_income(), TestData.Title_edit)


    def test_delete_income(self):
        main_page = MainPage(self.driver)
        main_page.click_income()
        self.driver.implicitly_wait(30)
        add_income_page = AddIncomePage(self.driver)
        add_income_page.type_price(TestData.Price)
        add_income_page.type_title(TestData.Title)
        add_income_page.type_category(TestData.Category)
        add_income_page.time_click()
        add_income_page.date_click()
        add_income_page.account_selector_click()
        self.driver.implicitly_wait(60)
        add_income_page.account_list_select()
        add_income_page.click_save_income()
        main_page = MainPage(self.driver)
        main_page.click_new_element()
        deleteEdit_page = EditDeleteIncome(self.driver)
        deleteEdit_page.delete_income()
        self.assertIsNone(main_page.new_title_element_add_income())


    # incomes/expenses podem ser editados e removidos

    # Lista de incomes e expenses salvos devem ser exibidos na tela Records. Para exibir registros de datas anteriores basta clicar no seletor Week (parte superior da tela à direita) e selecionar "All time"


if __name__ == '__main__':
    unittest.main()
