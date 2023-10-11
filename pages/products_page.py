from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def get_products_title(self):
        return WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, '.header_secondary_container .title'))
        ).text

    def is_logout_option_available(self):
        self.open_burger_menu()
        return WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.ID, 'logout_sidebar_link'))
        ).is_displayed()

    def open_burger_menu(self):
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.ID, 'react-burger-menu-btn'))
        ).click()

    def logout(self):
        self.open_burger_menu()
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.ID, 'logout_sidebar_link'))
        ).click()
