from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.ID, 'user-name').send_keys(username)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        self.driver.find_element(By.ID, 'login-button').click()

    def get_error_message(self):
        return WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, 'h3[data-test="error"]'))
        ).text

    def is_login_button_visible(self):
        return WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.ID, 'login-button'))
        ).is_displayed()
