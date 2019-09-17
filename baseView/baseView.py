# -*- coding:utf-8 -*-
__author__ = 'xiaoguo'

class BaseView(object):
    def __init__(self, driver):
        self.driver = driver

    # 返回当前页面符合条件的第一个节点，如果定位不到元素会报错
    def find_element(self, *location):
        return self.driver.find_element(*location)

    # 返回查找到的多个元素的列表，如果定位不到元素，则返回一个空的列表
    def find_elements(self, *location):
        return self.driver.find_elements(*location)

    # 返回屏幕的尺寸
    def get_screen_size(self):
        return self.driver.get_window_size()

    # 滑动操作
    def swipe(self, st_x, st_y, end_x, end_y, duration):
        return self.driver.swipe(st_x, st_y, end_x, end_y, duration)