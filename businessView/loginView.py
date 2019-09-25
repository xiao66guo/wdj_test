# -*- coding:utf-8 -*-
__author__ = 'xiaoguo'

from general.general_view import general_view
from general.xg_caps import appium_caps
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import logging

class login_view(general_view):
    # 主导航菜单
    navigation_element = (By.ID, 'com.wandoujia.phoenix2:id/w4')
    # 设置菜单
    setting_element = (By.ID, 'com.wandoujia.phoenix2:id/pp_item_setting')
    # 登录
    # login_element = (By.ID, 'com.wandoujia.phoenix2:id/ow')
    login_element = (By.ID, 'com.wandoujia.phoenix2:id/nr')
    # 退出登录
    logout_element = (By.ID, 'com.wandoujia.phoenix2:id/m9')
    # 立即登录
    loginImmediately_element = (By.ID, 'com.wandoujia.phoenix2:id/mf')
    # 用户名、密码
    username_element = (By.ID, 'com.wandoujia.phoenix2:id/l_')
    password_element = (By.ID, 'com.wandoujia.phoenix2:id/la')
    # 复选框
    checkBox_element = (By.ID, 'com.wandoujia.phoenix2:id/mw')
    # 登录按钮
    loginBtn_element = (By.ID, 'com.wandoujia.phoenix2:id/mf')

    def login_action(self, username, password):
        self.click_jumpBtn()
        self.click_cancelBtn()
        logging.info('=' * 10 + 'login_action' + '=' * 10)
        self.driver.find_element(*self.navigation_element).click()
        self.driver.find_element(*self.setting_element).click()
        try:
            element = self.driver.find_element(*self.login_element)
        except NoSuchElementException:
            pass
        else:
            element.click()
        try:
            out_element = self.driver.find_element(*self.logout_element)
            logging.info('Is logged in')
        except NoSuchElementException:
            pass
        else:
            out_element.click()
        self.driver.find_element(*self.loginImmediately_element).click()
        logging.info('username is：*************')
        self.driver.find_element(*self.username_element).send_keys(username)
        logging.info('password is：*************')
        self.driver.find_element(*self.password_element).send_keys(password)
        logging.info('check the box')
        self.driver.find_element(*self.checkBox_element).click()
        logging.info('click loginBtn')
        self.driver.find_element(*self.loginBtn_element).click()


if __name__ == '__main__':
    driver = appium_caps()
    # login = login_view(driver)
    # login.login_action('用户名', '密码')