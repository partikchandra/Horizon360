from tests_case.login.login_test import LoginTest
class LoginTest:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        try:
            LoginTest(self.driver).test_login()
        except Exception as e:
            print("Error", e)
