# 登录模块
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_framework.src.utils.config import Config, DRIVER_PATH, DATA_PATH
# from Test_framework.src.utils.log import logger
from Test_framework.src.utils.file_reader import ExcelReader


class LoGin(object):
    URL = Config().get('URL')
    excel = DATA_PATH + '\TestLogin.xlsx'
    phone = (By.XPATH, Config().get('phone'))
    Username = (By.ID, Config().get('Username'))
    password = (By.XPATH, Config().get('password'))
    # login_button = (By.XPATH, Config().get('login_button'))
    login_button = (By.XPATH, Config().get('login_button'))  # 登录页，登录按钮
    # quit = (By.XPATH, Config().get('quit'))
    digital = Config().get('digital')
    # driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
    # driver.maximize_window()
    # driver.get(URL)

    def __init__(self, driver):
        self.driver = driver
    # @classmethod
    # def sub_setUp(cls):
    #     cls.driver = driver
        # cls.driver.maximize_window()
        # cls.driver.get(LoGin.URL)
    #     # P = self.driver.driver
    #     # self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
    #     self.driver.maximize_window()
    #     self.driver.get(LoGin.URL)
    #     print(1)
    #
    # def sub_teardown(self):
    #     self.driver.close()

    def test_search(self):
        # self.driver.maximize_window()
        # self.driver.get(LoGin.URL)
        datas = ExcelReader(self.excel).data
        time.sleep(3)
        self.driver.find_element(*self.phone).clear()  # 清空用户名输入框
        self.driver.find_element(*self.password).clear()  # 清空密码输入框
        self.driver.find_element(*self.phone).send_keys(
            datas[LoGin.digital]['username'])  # 输入用户名（读取表格）
        self.driver.find_element(*self.password).send_keys(
            datas[LoGin.digital]['password'])  # 输入密码（读取表格）
        self.driver.find_element(*self.login_button).click()  # 登录页，点击登录按钮


if __name__ == '__main__':
    unittest.main()