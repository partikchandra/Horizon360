from selenium.webdriver.common.by import By
from utils.loadJson import laodjson

class signupPage:
    def __init__(self, driver):
        self.driver = driver
        self.savechanges = (By.XPATH, "//android.widget.Button")
        self.sinup_btn = (By.ID, "com.toro.horizon360:id/sign_up_text")
        self.first_name = (By.XPATH, "//android.widget.EditText[@resource-id='com.toro.horizon360:id/fui_first_name_et']")
        self.last_name = (By.ID, "com.toro.horizon360:id/fui_last_name_et")
        self.email = (By.ID, "com.toro.horizon360:id/fui_email_et")
        self.comp_name = (By.ID, "com.toro.horizon360:id/fui_company_name_et")
        self.password_field = (By.ID, "com.toro.horizon360:id/fui_password_et")
        self.conpassword_field = (By.ID, "com.toro.horizon360:id/fui_confirm_password_et")
        self.check_box = (By.ID, "com.toro.horizon360:id/fui_checkbox_terms")
        self.next_btn = (By.ID, "com.toro.horizon360:id/next_btn")
        self.pass_error = (By.XPATH, '//android.widget.TextView[@resource-id="com.toro.horizon360:id/textinput_error" and @text="Password must be at least 8 characters and contain at least one letter, one number, and one special character."]')

    # Functions to perform operations on Home page

    def loadData(file_path="config/data.json"):
        data = laodjson(file_path).load_users()
        screens = data["screens"]["signup"]
        user_key = "default_user"
        fNmae = screens[user_key]["fNmae"]
        lName = screens[user_key]["lName"]
        comName = screens[user_key]["comName"]
        email = screens[user_key]["email"]
        password = screens[user_key]["password"]
        confirm_password = screens[user_key]["confirm_password"]
