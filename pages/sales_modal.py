import time

from selenium.webdriver.common.by import By
from .base_page import BasePage


class SalesModal(BasePage):
    def check_modal(self, header_xpath, expected_text, error_message):
        assert expected_text in self.get_text((By.XPATH, header_xpath)), error_message

    def click_button(self, button_xpath):
        time.sleep(2)
        self.click_element((By.XPATH, button_xpath))

















# class SalesModal(BasePage):
#     HEADER_TEXT = (By.XPATH, "//h3/span[contains(text(), 'Продажа')]")
#     ORDERS_BUTTON = (By.XPATH, "//a/span[contains(text(), 'Заказы')]")
#
#     def check_modal(self):
#         assert "Продажа" in self.get_text(self.HEADER_TEXT), "Sales_modal sahifasi ochilmadi!"
#
#     def click_button(self):
#         time.sleep(2)
#         self.click_element(self.ORDERS_BUTTON)
