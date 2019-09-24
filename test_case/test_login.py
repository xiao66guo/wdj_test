# -*- coding:utf-8 -*-
__author__ = 'xiaoguo'

from businessView.loginView import login_view
from general.xgunit import startAndEnd
import logging, unittest

class TestLogin(startAndEnd):
    csf_file = '../data/account.csv'
    def test_login_first(self):
        logging.info('-' * 10 + 'first' + '-' * 10)
        first = login_view(self.driver)
        data = first.get_csv_data(self.csf_file, 1)
        first.login_action(data[0], data[1])

    @unittest.skip('skip-test_login_second')
    def test_login_second(self):
        logging.info('=' * 10 + 'second' + '=' * 10)
        second = login_view(self.driver)
        data = second.get_csv_data(self.csf_file, 2)
        second.login_action(data[0], data[1])

    @unittest.skip('skip-test_login_third')
    def test_login_third(self):
        logging.info('*' * 10 + 'third' + '*' * 10)
        third = login_view(self.driver)
        data = third.get_csv_data(self.csf_file, 3)
        third.login_action(data[0], data[1])


if __name__ == '__main__':
    unittest.main()

