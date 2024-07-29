import pytest
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# @pytest.fixture(scope='function')
class LoginTest:
    def __init__(self, driver, platform):
        self.driver = driver
        self.platform = platform
        if platform == 'Android':            
            self.username = (By.ID, "com.toro.horizon360:id/email_edit_text")
            self.password = (By.ID, "com.toro.horizon360:id/password_edit_text")
            self.sign_in_button = (By.ID, "com.toro.horizon360:id/sign_in_btn")
            self.forgot = (By.ID, "com.toro.horizon360:id/al_forgot_password_txt")
            self.loadingIndicator = (By.XPATH, "//android.widget.ImageView")
            self.savechanges = (By.XPATH, "//android.widget.Button")
            self.invalid_button = (By.ID, "com.toro.horizon360:id/positive_btn")
        elif platform == 'iOS':
            self.username = (By.ID, "com.toro.horizon360:id/email_edit_text")
            self.password = (By.ID, "com.toro.horizon360:id/password_edit_text")
            self.sign_in_button = (By.ID, "com.toro.horizon360:id/sign_in_btn")
            self.forgot = (By.ID, "com.toro.horizon360:id/al_forgot_password_txt")
            self.loadingIndicator = (By.XPATH, "//android.widget.ImageView")
            self.savechanges = (By.XPATH, "//android.widget.Button")
            self.invalid_button = (By.ID, "com.toro.horizon360:id/positive_btn")
        else:
             raise ValueError("Error in the init of login platform")
    
    def load_users(self, file_path):
            with open(file_path, 'r') as file:
                return json.load(file)

    def test_login(self, file_path="config/data.json"):
            data = self.load_users(file_path)
            users = data['users']
            screens = data["screens"]["login"]

            for user_key in screens:
                user = screens[user_key]["username"]
                password = screens[user_key]["password"]

                if user_key == "QA":
                    self.login_QA(user, password)
                # elif  user_key ==  "default_user":
                #     self.login_default(user, password)
                # else:
                #     self.login_another(user, password)

    def login_default(self, user, password):
            try:
                WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.username)).send_keys(user)
                WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.password)).send_keys(password)
                WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.sign_in_button)).click()
                WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located(self.loadingIndicator))
            except Exception as e:
                print("Error", e)

    def login_QA(self, user, password):
            try:
                WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.savechanges)).click()
                WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.username)).send_keys(user)
                WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.password)).send_keys(password)
                WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.sign_in_button)).click()
                WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located(self.loadingIndicator))
            except Exception as e:
                print("Error", e)
    def login_another(self, user, password):
            try:
                WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.username)).send_keys(user)
                WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.password)).send_keys(password)
                WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.sign_in_button)).click()

            except Exception as e:
                print("Error", e)

def test_login(driver, platform):
     login_test = LoginTest(driver, platform)
     login_test.test_login()