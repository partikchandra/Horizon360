import pytest

@pytest.fixture(scope="module")
def driver():
    from utils.driver_factory import get_driver
    driver = get_driver()
    yield driver
    driver.quit()   
