import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver_factory import get_driver
from page_objects.signupPage import signupPage as signup

@pytest.fixture(scope="module")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()
    

def test_signup(driver):
    try:
        signup.loadData()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(signup(driver).savechanges)).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(signup(driver).sinup_btn)).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(signup(driver).first_name)).send_keys(signup.loadData.fNmae)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(signup(driver).last_name)).send_keys(signup.loadData.lName)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(signup(driver).email)).send_keys(signup.loadData.email)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(signup(driver).comp_name)).send_keys(signup.loadData.comName)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(signup(driver).password_field)).send_keys(signup.loadData.password)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(signup(driver).conpassword_field)).send_keys(signup.loadData.confirm_password)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(signup(driver).check_box)).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(signup(driver).next_btn)).click()
        result = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(signup(driver).pass_error)).text
        if result:
            return "Pass"
        else:
            return "Fail"              
    except Exception as e:
            print(e)


        