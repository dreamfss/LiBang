# coding = utf-8
import time
import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_framework.src.utils.config import Config, DRIVER_PATH, DATA_PATH, LOG_PATH
from Test_framework.src.utils.login import LoGin
from Test_framework.src.utils.log import logger
from Test_framework.src.utils.file_reader import ExcelReader
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class Test_Login(unittest.TestCase):
    # 页面元素定位（获取Config中配置）
    URL = Config().get('URL')  # 获取URL
    excel = DATA_PATH + '\TestLogin.xlsx'  # 所用表格
    phone = (By.XPATH, Config().get('phone'))  # 用户名输入框
    Username = (By.XPATH, Config().get('Username'))  # 登录后，用户名
    password = (By.XPATH, Config().get('password'))  # 密码输入框
    # order = (By.XPATH, Config().get('order'))  #订单页签
    order = (By.XPATH, Config().get('order'))  #订单页签
    new_order = (By.XPATH, Config().get('new_order'))  #新建订单
    uesr_search = (By.XPATH, Config().get('uesr_search'))  #新建订单，用户输入框
    search_user = (By.XPATH, Config().get('search_user'))  #新建订单，搜索按钮
    digital = Config().get('digital')  #表格中行数

    @classmethod
    def sub_setUp(cls):
        # 调用登录模块中driver
        cls.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        cls.driver.maximize_window()
        cls.driver.get(Test_Login.URL)

    def sub_tearDown(self):
        # 关闭游览器、命令框
        self.driver.quit()

    def test_search(self):
        try:
            self.sub_setUp()  # 调用sub_setUp方法
            p = LoGin(self.driver)  #调用登录类，并定位driver
            p.test_search()  #调用登录方法
            datas = ExcelReader(self.excel).data
            print(2)
            WebDriverWait(self.driver, 10).until(lambda driver:  #定位设置框
                                                 self.driver.find_element(*self.Username))
            print(3)
            WebDriverWait(self.driver, 10).until(lambda driver:  # 定位订单框
                                                 self.driver.find_element(*self.order))
            print(4.1)
            above = self.driver.find_element(*self.order)  #定位加入订单位置
            ActionChains(self.driver).move_to_element(above).click().perform()  #待元素显示，点击元素
            print(4)
            self.driver.find_element(*self.new_order).click()
            self.driver.find_element(*self.uesr_search).send_keys(datas[Test_Login.digital]["user"])
            logger.info('登录成功')  # 登录成功日志
            self.sub_tearDown()  # 调用退出方法
        except Exception as msg:
            # 代码执行错误时，打印图片
            script = os.path.basename(__file__)[:-3]   #获取用例名，去除.py
            nowTime = time.strftime("%Y.%m.%d.%H.%M.%S") + "." + script  # 图片名称格式
            self.driver.get_screenshot_as_file(
                (LOG_PATH + '//%s.png') % nowTime)  # 截屏图片
            logger.info(script + ".%s" % msg)
            self.sub_tearDown()  # 调用退出方法


if __name__ == '__main__':
    unittest.main()
