# -*- coding:utf-8 -*-
__author__ = 'xiaoguo'

from BSTestRunner import BSTestRunner
import logging, unittest, time

# 指定测试用例和测试报告的路径
test_dir = '../test_case'
report_dir = '../reports'

# 加载登录测试用例（pattern 参数可以控制运行不同模块的测试用例，如：pattern='xg*.py',就表示可以运行指定路径下的以xg开头的所有模块)
discover = unittest.defaultTestLoader.discover(test_dir, pattern='xg_login.py')

# 定义测试报告的文件格式
now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = report_dir + '/' + now + 'wdj_TestReport.html'

# 执行测试用例并生成测试报告
with open(report_name, 'wb') as file:
    runner = BSTestRunner(stream=file, title='Wdj Test Report', description='Wdj Android app test report')
    logging.info('start run testcase')
    runner.run(discover)