import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


class TestSauceDemoLoginLogout(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.login_page = LoginPage(cls.driver)
        cls.products_page = ProductsPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_valid_login(self):
        self.driver.get('https://www.saucedemo.com/')
        self.login_page.login('standard_user', 'secret_sauce')
        products_title = self.products_page.get_products_title()
        self.assertEqual(products_title, 'Products', msg="Valid login failed, 'Products' title not found.")

    def test_invalid_login(self):
        self.driver.get('https://www.saucedemo.com/')
        self.login_page.login('invalid_username', 'invalid_password')
        error_message = self.driver.find_element(By.CSS_SELECTOR, 'h3[data-test="error"]').text
        self.assertEqual(error_message, 'Epic sadface: Username and password do not match any user in this service', msg="Invalid login failed, error message mismatch or not found.")

    def test_logout(self):
        self.driver.get('https://www.saucedemo.com/')
        self.login_page.login('standard_user', 'secret_sauce')
        self.products_page.open_burger_menu()
        self.products_page.logout()

        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.ID, 'login-button'))
        )

        login_button_text = self.driver.find_element(By.ID, 'login-button').get_attribute('value')
        self.assertEqual(login_button_text, 'Login', msg="Logout failed, 'Login' button text not found.")


if __name__ == '__main__':
    unittest.main()
