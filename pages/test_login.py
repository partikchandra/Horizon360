import pytest
from tests_case.login.login_test import LoginTest
from tests_case.login.signup import signup
from utils.driver_factory import get_driver

@pytest.fixture(scope="module")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_login(driver):
    try:
        LoginTest(driver).test_login()
    except Exception as e:
        pytest.fail(f"Test failed with exception: {e}")

def test_signup(driver):
    try:
        signup(driver).test_signup()
    except Exception as e:
        pytest.fail(f"Test failed with exception: {e}")

def run_login_tests():
    test_login(driver())
    test_signup(driver())
