from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def get_products_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.header_secondary_container .title').text

    def open_burger_menu(self):
        self.driver.find_element(By.ID, 'react-burger-menu-btn').click()

    def logout(self):
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.ID, 'logout_sidebar_link'))
        )

        self.driver.find_element(By.ID, 'logout_sidebar_link').click()
