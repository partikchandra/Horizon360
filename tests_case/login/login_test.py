import pytest
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture(scope="module")
class LoginTest:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, "com.toro.horizon360:id/email_edit_text")
        self.password = (By.ID, "com.toro.horizon360:id/password_edit_text")
        self.sign_in_button = (By.ID, "com.toro.horizon360:id/sign_in_btn")
        self.forgot = (By.ID, "com.toro.horizon360:id/al_forgot_password_txt")
        self.sign_up_button = (By.ID, "com.toro.horizon360:id/sign_up_text")

    def load_users(self,file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    def test_login(self):
        users = self.load_users('config/data.json')
        for user in users:
            self.login(user['user'], user['pass'])
            time.sleep(2)

    def login(self, user, password):
        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.username)).send_keys(user)
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.password)).send_keys(password)
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.sign_in_button)).click()
        except Exception as e:
            print("Error", e)



