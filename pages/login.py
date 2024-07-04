from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.login.sigup import signup
from tests.login.login_test import login_test

# rpu2307+h251@gmail.com & ttt@0000

class login:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, "com.toro.horizon360:id/email_edit_text")
        self.password = (By.ID, "com.toro.horizon360:id/password_edit_text")
        self.Sign_Inbutton = (By.ID, "com.toro.horizon360:id/sign_in_btn")
        self.forgot = (By.ID, "com.toro.horizon360:id/al_forgot_password_txt")
        self.signUpbutton = (By.ID, "com.toro.horizon360:id/sign_up_text")
    
    def onboard(self):

        try:
            
            login_test(self.driver).test_app()
            
            # Sign Up
            # signup(self.driver).signup()

        except Exception as e:
            print("Error ", e)
