from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.login.sigup import signup
import json
import time

# rpu2307+h251@gmail.com & ttt@0000

class login_test:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, "com.toro.horizon360:id/email_edit_text")
        self.password = (By.ID, "com.toro.horizon360:id/password_edit_text")
        self.Sign_Inbutton = (By.ID, "com.toro.horizon360:id/sign_in_btn")
        self.forgot = (By.ID, "com.toro.horizon360:id/al_forgot_password_txt")
        self.signUpbutton = (By.ID, "com.toro.horizon360:id/sign_up_text")
    
    
    
    def test_app(self, users):
        for user in users:
            loginfunc(self.driver, user['user'], user['pass'])
            # WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((self.Sign_Inbutton))).click()
            time.sleep(3)


        def loginfunc(self, user, password):

            try:
                WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((self.username))).send_keys(user)
                WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((self.password))).send_keys(password)
                WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((self.Sign_Inbutton))).click()
                
            except Exception as e:
                print("Error ", e)
