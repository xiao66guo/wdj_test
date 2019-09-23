# -*- coding:utf-8 -*-
__author__ = 'xiaoguo'

from general.xg_caps import appium_caps
import unittest, logging
from time import sleep

class startAndEnd(unittest.TestCase):

    def setUp(self):
        logging.info('-' * 10 + 'setUp' + '-' * 10)
        self.driver = appium_caps()

    def tearDown(self):
        logging.info('=' * 10 + 'tearDown' + '=' * 10)
        sleep(5)
        self.driver.close_app()