import unittest, time, os
from builtins import id

import self as self
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from datetime import date
from time import sleep
import warnings


class AndroidBudget(unittest.TestCase):

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

        self.driver.implicitly_wait(30)

        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()

        # clicar em budget
        budget = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@text, 'Budgets')]")
        budget.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/budgetNameEdit')
        name.set_text("energia")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.set_text("500")

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()

        self.assertEqual("energia", self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'energia')]").get_attribute('text'))

    def test_app_budget_add_nome_invalido(self):

        self.driver.implicitly_wait(30)

        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()

        # clicar em budget
        budget = self.driver.find_element(By.ID, 'protect.budgetwatch:id/image')
        budget.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/budgetNameEdit')
        name.set_text("")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.set_text("100")

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()

        self.assertEqual('Budget type is empty',
                         self.driver.find_element(By.ID, 'protect.budgetwatch:id/snackbar_text').get_attribute('text'))

    def test_app_budget_add_valor_invalido(self):

        self.driver.implicitly_wait(30)

        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()

        # clicar em budget
        budget = self.driver.find_element(By.ID, 'protect.budgetwatch:id/image')
        budget.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/budgetNameEdit')
        name.set_text("test")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.set_text("abcdefg")

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()

        self.assertEqual('Budget value is empty',
                         self.driver.find_element(By.ID, 'protect.budgetwatch:id/snackbar_text').get_attribute('text'))

    def test_app_budget_add_campos_vazios(self):

        self.driver.implicitly_wait(30)

        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()

        # clicar em budget
        budget = self.driver.find_element(By.ID, 'protect.budgetwatch:id/image')
        budget.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()

        self.assertEqual('Budget value is empty',
                         self.driver.find_element(By.ID, 'protect.budgetwatch:id/snackbar_text').get_attribute('text'))

    def test_app_budget_add_nome_acima_30(self):

        self.driver.implicitly_wait(30)

        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()

        # clicar em budget
        budget = self.driver.find_element(By.ID, 'protect.budgetwatch:id/image')
        budget.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/budgetNameEdit')
        name.set_text("nome de uma gasto com mais de 30 carácter")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.set_text("30")

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()

        self.assertEqual('Budget type is empty',
                         self.driver.find_element(By.ID, 'protect.budgetwatch:id/snackbar_text').get_attribute('text'))

    def test_app_budget_add_valor_acima_10(self):

        self.driver.implicitly_wait(30)

        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()

        # clicar em budget
        budget = self.driver.find_element(By.ID, 'protect.budgetwatch:id/image')
        budget.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/budgetNameEdit')
        name.set_text("Gasto 1")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.set_text("12345678910")

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()

        self.assertEqual('Budget value is empty',
                         self.driver.find_element(By.ID, 'protect.budgetwatch:id/snackbar_text').get_attribute('text'))

    def test_app_budget_edit(self):

        self.driver.implicitly_wait(30)

        actions = TouchAction(self.driver)

        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()

        # clicar em budget
        budget = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@text, 'Budgets')]")
        budget.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/budgetNameEdit')
        name.set_text("energia")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.set_text("500")

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()

        # Long click no budget salvo
        budgetEdit = self.driver.find_element(By.XPATH,
                                          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout/android.widget.LinearLayout")

        actions.long_press(budgetEdit)
        actions.perform()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidBudget)
    unittest.TextTestRunner(verbosity=2).run(suite)
