import pytest
from pages.test_login import run_login_tests
# from pages.other_page import run_other_tests  

def main():
    run_login_tests()
    # run_other_tests()  

if __name__ == "__main__":
    pytest.main(["-v", "--html=report.html"])
