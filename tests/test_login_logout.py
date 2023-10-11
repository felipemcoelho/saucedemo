import unittest
from selenium import webdriver
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

    def setUp(self):
        self.driver.get('https://www.saucedemo.com/')

    def test_valid_login(self):
        self.login_page.login('standard_user', 'secret_sauce')
        products_title = self.products_page.get_products_title()
        self.assertEqual(products_title, 'Products', msg="Valid login failed, 'Products' title not found.")
        self.assertTrue(self.products_page.is_logout_option_available(), msg="Logout option not available.")

    def test_invalid_login(self):
        self.login_page.login('invalid_username', 'invalid_password')
        error_message = self.login_page.get_error_message()
        self.assertEqual(error_message, 'Epic sadface: Username and password do not match any user in this service',
                         msg="Invalid login failed, error message mismatch or not found.")

    def test_empty_username(self):
        self.login_page.login('', 'secret_sauce')
        error_message = self.login_page.get_error_message()
        self.assertEqual(error_message, 'Epic sadface: Username is required', msg="Error message mismatch.")

    def test_empty_password(self):
        self.login_page.login('standard_user', '')
        error_message = self.login_page.get_error_message()
        self.assertEqual(error_message, 'Epic sadface: Password is required', msg="Password message mismatch.")

    def test_wrong_username_correct_password(self):
        self.driver.get('https://www.saucedemo.com/')
        self.login_page.login('wrong_username', 'secret_sauce')
        error_message = self.login_page.get_error_message()
        self.assertEqual(error_message, 'Epic sadface: Username and password do not match any user in this service',
                         msg="Invalid login failed, error message mismatch or not found.")

        def test_logout(self):
            self.login_page.login('standard_user', 'secret_sauce')
            self.products_page.logout()
            self.assertTrue(self.login_page.is_login_button_visible(), msg="Login button is not visible after logout.")

    if __name__ == '__main__':
        unittest.main()
