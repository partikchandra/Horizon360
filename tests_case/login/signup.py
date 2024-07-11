from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.loadJson import laodjson
import time

# rpu2307+h251@gmail.com & ttt@0000

class signup:
    def __init__(self, driver):
        self.driver = driver
        self.sinup_btn = (By.ID, "com.toro.horizon360:id/sign_up_text")
        self.first_name = (By.ID, "com.toro.horizon360:id/fui_first_name_et")
        self.last_name = (By.ID, "com.toro.horizon360:id/fui_last_name_et")
        self.email = (By.ID, "com.toro.horizon360:id/fui_email_et")
        self.comp_name = (By.ID, "com.toro.horizon360:id/fui_company_name_et")
        self.password_field = (By.ID, "com.toro.horizon360:id/fui_password_et")
        self.conpassword_field = (By.ID, "com.toro.horizon360:id/fui_confirm_password_et")
        self.check_box = (By.ID, "com.toro.horizon360:id/fui_checkbox_terms")
        self.next_btn = (By.ID, "com.toro.horizon360:id/next_btn")
        self.pass_error = (By.XPATH, '//android.widget.TextView[@resource-id="com.toro.horizon360:id/textinput_error" and @text="Password must be at least 8 characters and contain at least one letter, one number, and one special character."]')
    
    def test_signup(self, file_path="config/data.json"):
        data = laodjson(file_path).load_users()
        screens = data["screens"]["signup"]
        user_key = "default_user"
        fNmae = screens[user_key]["fNmae"]
        lName = screens[user_key]["lName"]
        comName = screens[user_key]["comName"]
        email = screens[user_key]["email"]
        password = screens[user_key]["password"]
        confirm_password = screens[user_key]["confirm_password"]
        self.test(fNmae, lName, comName, email, password, confirm_password)

    def test(self, fNmae, lName, comName, email, password, confirm_password):
        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.sinup_btn)).click()
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.first_name)).send_keys(fNmae)
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.last_name)).send_keys(lName)
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.email)).send_keys(email)
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.comp_name)).send_keys(comName)
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.password_field)).send_keys(password)
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.conpassword_field)).send_keys(confirm_password)
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.check_box)).click()
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.next_btn)).click()
            result = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.pass_error)).text
            if result:
                return "Pass"
            else:
                return "Fail"

            
            
        except Exception as e:
            print(e)
