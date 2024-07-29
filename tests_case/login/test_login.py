import pytest
from Horizon360.page_objects.test_Loginpage import LoginTest
from tests_case.login.test_signup import signup
from utils.driver_factory import get_driver

@pytest.fixture(scope="module")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.mark.run(order=1)
def test_login(driver):
    try:
        LoginTest(driver).test_login()
    except Exception as e:
        pytest.fail(f"Test failed with exception: {e}")

