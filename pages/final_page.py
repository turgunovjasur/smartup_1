from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from .base_page import BasePage


class FinalPage(BasePage):
    def fill_form(self, payment_type, status, payment_type_input_xpath, payment_elem_xpath, status_input_xpath, status_elem_xpath):
        self.new_input((By.XPATH, payment_type_input_xpath), payment_type, (By.XPATH, payment_elem_xpath))
        try:
            self.choice((By.XPATH, status_input_xpath), (By.XPATH, status_elem_xpath))
        except TimeoutException:
            print("Status tanlashda xatolik yuz berdi")
            self.take_screenshot("status_selection_error")

    def click_save_button(self, save_button_xpath, yes_button_xpath):
        self.click_element((By.XPATH, save_button_xpath))
        self.click_element((By.XPATH, yes_button_xpath))






















# class FinalPage(BasePage):
#     PAYMENT_TYPE_INPUT = (By.XPATH, '//*[@id="kt_content"]/div[2]/div/b-page/div/div/div/div/div/form[3]/div/div[2]/div/div/div[2]/b-input/div/div[1]/div/input')
#     PAYMENT_ELEM = (By.XPATH, '//*[@id="kt_content"]/div[2]/div/b-page/div/div/div/div/div/form[3]/div/div[2]/div/div/div[2]/b-input/div/div[2]/div[1]/div/div')
#     STATUS_INPUT = (By.XPATH, '//*[@id="kt_content"]/div[2]/div/b-page/div/div/div/div/div/form[3]/div/div[3]/div/div/div[6]/div')
#     STATUS_ELEM = (By.XPATH, '//*[@id="ui-select-choices-row-4-0"]/span')
#     WAYBILL_INPUT = (By.XPATH, "//div/input[@placeholder='Пароль']")
#
#     SAVE_BUTTON = (By.XPATH, "//span/t[contains(text(), 'Сохранить')]")
#     YES_BUTTON = (By.XPATH, "//div/button[contains(text(), 'да')]")
#
#     def fill_form(self, payment_type, status):
#         self.new_input(self.PAYMENT_TYPE_INPUT, payment_type, self.PAYMENT_ELEM)
#         try:
#             self.choice(self.STATUS_INPUT, self.STATUS_ELEM)
#         except TimeoutException:
#             print("Status tanlashda xatolik yuz berdi")
#             self.take_screenshot("status_selection_error")
#
#     def click_save_button(self):
#         self.click_element(self.SAVE_BUTTON)
#         self.click_element(self.YES_BUTTON)
