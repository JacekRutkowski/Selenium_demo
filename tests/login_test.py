from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
from pages.my_account_page import MyAccountPage

@pytest.mark.usefixtures("setup")
class TestLogIn:

    def test_log_in_passed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in("test1@test.com", "Klamra12#3")

        assert my_account_page.is_logout_link_displayed()

    def test_log_in_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in("test1@test.coml", "Klamra12#311")

        assert "ERROR: Incorrect username or password." in my_account_page.get_error_msg()
