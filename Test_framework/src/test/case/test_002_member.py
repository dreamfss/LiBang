# coding = utf-8
import time
import unittest
import os
from selenium import webdriver
from Test_framework.src.utils.login import LoGin
from selenium.webdriver.common.by import By
from Test_framework.src.utils.config import Config, DRIVER_PATH, DATA_PATH, LOG_PATH
from Test_framework.src.utils.config import Config
from Test_framework.src.utils.log import logger


class Test_Member(unittest.TestCase):
    member_centre = (By.XPATH, Config().get('member_centre'))
    prompt = (By.XPATH, Config().get('prompt'))
    # driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')

    @classmethod
    def sub_setUp(cls):
        # 调用登录模块中driver
        cls.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        cls.driver.maximize_window()
        cls.driver.get(LoGin.URL)
        print("这段有输出")

    def sub_tearDown(self):
        self.driver.quit()

    def test_search(self):
        try:
            self.sub_setUp()  # 调用sub_setUp方法
            p = LoGin(self.driver)
            p.test_search()
            print(10)
            # LoGin()
            # print(11)
            time.sleep(2)
            self.driver.find_element(*self.member_centre).click()
            test = self.driver.find_element(*self.prompt).text
            links = test[3:7]
            print(links)
            if links == Config().get('links'):
                self.sub_tearDown()
                logger.info('会员中心登录成功')
        except Exception as msg:
            # 代码执行错误时，打印图片
            script = os.path.basename(__file__)[:-3]  #获取用例名，去除.py
            nowTime = time.strftime("%Y.%m.%d.%H.%M.%S") + "." + script  # 图片名称格式
            self.driver.get_screenshot_as_file(
                (LOG_PATH + '//%s.png') % nowTime)  # 截屏图片
            logger.info(script + ".%s" % msg)
            self.sub_tearDown()  # 调用退出方法


if __name__ == '__main__':
    unittest.main()
