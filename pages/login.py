from tests_case.login.login_test import LoginTest
class login:
    def __init__(self, driver):
        self.driver = driver

    def login(self, user):
        try:
            LoginTest(self.driver).test_login(user)
        except Exception as e:
            print("Error", e)
