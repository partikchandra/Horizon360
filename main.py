from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

from utils.driver_factory import get_driver
from pages.login import login
@pytest.fixture(scope="module")


def main():
    driver = get_driver()
    yield driver
    # Policy Page
    # WebDriverWait(driver,  20).until(EC.element_to_be_clickable(By.XPATH, '//android.widget.TextView[@text="Save Changes"]')).click()

    try: 
        login(driver).login()

    except Exception as e:
        print(e)

    # Close the driver
    driver.quit()  

if __name__ == "__main__":
    main()