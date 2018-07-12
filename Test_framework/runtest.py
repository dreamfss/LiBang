# coding = utf-8
import unittest
import time
from Test_framework.src.utils.log import logger
# from selenium import webdriver
from Test_framework.src.utils.config import REPORT_PATH
from Test_framework.src.utils.HTMLTestRunner import HTMLTestRunner
# from Test_framework.src.utils.config import DRIVER_PATH
# from Test_framework import runtest


def all_case():
    testunit = unittest.TestSuite()
    # -case_dir:这个是待执行用例的目录。
    # -pattern：这个是匹配脚本名称的规则，test*.py意思是匹配test开头的所有脚本。
    # -top_level_dir：这个是顶层目录的名称，一般默认等于None就行了。
    test_dir = 'D:\\TestCase\\Hypweb.Yili\\Test_framework\\src\\test\\case'
    suite = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py', top_level_dir=None)
    # 循环test_dir = 指定目录下，所有脚本命名格式为:pattern = test*.py 的脚本
    for test_suite in suite:
        for test_case in test_suite:
            testunit.addTest(test_case)
    return testunit
# alltestnames = rentest()

if __name__ == '__main__':
    # 执行用例
    try:
        runner = unittest.TextTestRunner()
        # 生成报告的目录
        filename = REPORT_PATH + '\\report.html'
        with open(filename, 'wb') as f:
            runner = HTMLTestRunner(f, verbosity=2, title='测试报告', description='修改html报告')
            runner.run(all_case())
    except Exception as msg:
        # 打印日志
        nowTime = time.strftime("%Y%m%d.%H.%M.%S") + ".test"
        logger.exception("%s" % msg)
        # test_suite.get_screenshot_as_file("D:\\TestCase\\Hypweb.Frame\\Test_framework\\log\\log%s.png" % nowTime)
        # 捕捉到了异常，但是又想重新引发它(传递异常)，可以使用不带参数的raise语句即可：